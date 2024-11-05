"""
(저자: Hepheir <hepheir@gmail.com>)

이 모듈은 OJ에 업로드할 수 있는 형식으로 테스트케이스들을 생성합니다.

`Problem` 클래스를 상속받아 문제를 정의하고, `testcase` 메서드를 이용하여 테스트케이스를 생성합니다.

사용 예시:

```python
import pathlib
from oj import Problem


BASE_DIR = pathlib.Path(__file__).parent.resolve()

problem = Problem(answer_file=BASE_DIR/'solution.py')

with problem.testcase('1') as sys:
    sys.stdin.write('1 2\\n')

with problem.testcase('2', manual=True) as sys:
    sys.stdin.write('1 2\\n')
    sys.stdout.write('3\\n')

problem.save('problem.zip')
```
"""

from __future__ import annotations

import hashlib
import io
import json
import logging
import os
import pathlib
import random
import subprocess
import tempfile
import time
import typing
import zipfile


__author__ = 'Hepheir <hepheir@gmail.com>'
__version__ = '0.2.3'

__all__ = ['Problem']


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)


PathLike = typing.Union[str, pathlib.Path]


class Problem:
    FILENAME_INFO = 'info'

    def __init__(self, answer_file: typing.Optional[PathLike] = None) -> None:
        self._spj = False
        self._testcases: typing.Dict[str, _TestCase] = dict()
        self._answer_file = answer_file

    def __answer__(self, stdin: typing.TextIO, stdout: typing.TextIO) -> None:
        """Generate output data from input data.

        This method is used to generate output data from input data.
        You can override this method to generate output data from input data.
        """
        assert self._answer_file is not None, (
            "자동으로 생성되는 정답을 사용하려면, 아래의 항목 중 하나를 \n"
            "1. 생성자의 answer_file 에 정답 풀이 파일을 지정\n"
            "2. __answer__ 메서드를 오버라이드하여 정답을 생성하는 코드를 작성\n"
            "3. testcase 메서드의 manual 인자를 True로 설정하여 수동으로 출력을 생성\n"
        )
        assert pathlib.Path(self._answer_file).exists(), (
            f"{self._answer_file} 파일이 존재하지 않아 정답을 자동으로 생성할 수 없습니다."
        )
        answer_file = pathlib.Path(self._answer_file)
        with tempfile.TemporaryDirectory() as dirname:
            dirpath = pathlib.Path(dirname)
            stdin_file = str(dirpath / '1.in')
            stdout_file = str(dirpath / '1.out')
            with open(stdin_file, 'w') as f:
                f.write(stdin.read())
            subprocess.run(
                args=['python3', str(answer_file)],
                stdin=open(stdin_file, 'r'),
                stdout=open(stdout_file, 'w'),
                text=True,
                env={
                    'PYDEVD_DISABLE_FILE_VALIDATION': '1',
                },
            )
            with open(stdout_file, 'r') as f:
                stdout.write(f.read())


    def testcase(self, name: str, manual=False) -> _BaseTestCaseGenerator:
        """`with`구문을 이용하여 새로운 테스트케이스를 생성합니다.

        만약 `__answer__` 메서드를 오버라이드 하였거나,
        생성자에 `answer_file`을 지정하였다면,
        테스트케이스의 출력을 자동으로 생성할 수 있습니다.

        `answer_file`을 지정하는 경우:

        >>> problem = Problem(answer_file='solution.py')
        >>> with problem.testcase('1') as sys:
        ...     sys.stdin.write('1 2\\n')

        `__answer__` 메서드를 오버라이드 하는 경우:

        >>> class MyProblem(Problem):
        ...     def __answer__(self, stdin: typing.TextIO, stdout: typing.TextIO) -> None:
        ...         A, B = map(int, stdin.readline().split())
        ...         stdout.write(str(A+B)+'\\n')
        >>> problem = MyProblem()
        >>> with problem.testcase('1') as sys:
        ...     sys.stdin.write('1 2\\n')

        테스트케이스의 출력을 수동으로 생성하려면 `manual`을 `True`로 설정하세요.
        이 때에는 `stdout`을 직접 작성해야 합니다.

        >>> with problem.testcase('2', manual=True) as sys:
        ...     sys.stdin.write('1 2\\n')
        ...     sys.stdout.write('3\\n')

        Args:
            name: 테스트케이스의 이름. (예: '1', '2', '3')
            manual: 만약 `True`이면, 테스트케이스의 출력을 수동으로 생성해야합니다.
        """
        if manual:
            return _ManualTestCaseGenerator(self, name)
        return _AutomaticTestCaseGenerator(self, name)

    def save(self, zipname: PathLike = None, dirname: PathLike = None) -> None:
        """OJ에 업로드할 수 있는 형식으로 테스트케이스들을 압축합니다."""
        assert dirname is not None or zipname is not None, "dirname or zipname must be specified"
        if dirname is not None:
            os.makedirs(dirname, exist_ok=True)
            self._save_dir(dirname)
        if zipname is not None:
            self._save_zip(zipname)

    def _save_dir(self, dirpath: pathlib.Path) -> None:
        data = {
            "spj": self._spj,
            "testcases": {
                name: obj.save(dirpath) for name, obj in self._testcases.items()
            },
        }
        with open(dirpath/self.FILENAME_INFO, 'w') as f:
            json.dump(data, f, ensure_ascii=True, indent=4)

    def _save_zip(self, zippath: pathlib.Path) -> None:
        with tempfile.TemporaryDirectory() as dirname:
            dirpath = pathlib.Path(dirname)
            self._save_dir(dirpath)
            with zipfile.ZipFile(zippath, 'w') as fzip:
                for fname in os.listdir(dirpath):
                    fzip.write(filename=dirpath/fname, arcname=fname)


class _TestCase:
    FILENAME_INPUT = '{name}.in'
    FILENAME_OUTPUT = '{name}.out'

    def __init__(self, name: str) -> None:
        self._name = name
        self._in = io.TextIOWrapper(io.BytesIO())
        self._out = io.TextIOWrapper(io.BytesIO())

    @property
    def stdin(self) -> io.TextIOWrapper:
        """input stream."""
        return self._in

    @property
    def stdout(self) -> io.TextIOWrapper:
        """output stream."""
        return self._out

    def save(self, problem_dir: pathlib.Path) -> dict:
        fname_in = problem_dir / self.FILENAME_INPUT.format(name=self._name)
        fname_out = problem_dir / self.FILENAME_OUTPUT.format(name=self._name)
        self.seek()
        text_in = self.stdin.read()
        text_out = self.stdout.read()
        with open(fname_in, 'w') as f:
            f.write(text_in)
        with open(fname_out, 'w') as f:
            f.write(text_out)
        return {
            "input_name": str(fname_in),
            "output_name": str(fname_out),
            "input_size": len(text_in),
            "output_size": len(text_out),
            "stripped_output_md5": self.stripped_output_md5(text_out),
        }

    def seek(self) -> None:
        self.stdin.seek(0, io.SEEK_SET)
        self.stdout.seek(0, io.SEEK_SET)

    def stripped_output_md5(self, text: str) -> str:
        text = os.linesep.join([line.rstrip() for line in text.splitlines()])
        md5 = hashlib.md5()
        md5.update(text.strip().encode())
        return md5.hexdigest()


class _BaseTestCaseGenerator:
    def __init__(self, problem: Problem, name: str) -> None:
        self.problem = problem
        self.name = name
        self.obj = _TestCase(name)

    def __enter__(self) -> _TestCase:
        random.seed(self.name)
        return self.obj

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.problem._testcases[self.name] = self.obj
        return False


class _ManualTestCaseGenerator(_BaseTestCaseGenerator):
    pass


class _AutomaticTestCaseGenerator(_BaseTestCaseGenerator):
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        logging.info(f'테스트케이스 {self.name} 의 출력을 자동으로 생성 시작.')
        st = time.time()
        self.obj.seek()
        self.problem.__answer__(self.obj.stdin, self.obj.stdout)
        et = time.time()
        logging.info(f'테스트케이스 {self.name} 의 출력을 자동으로 생성 완료. ({(et-st)*1000:.0f} ms 소요됨.)')
        return super().__exit__(exc_type, exc_value, traceback)
