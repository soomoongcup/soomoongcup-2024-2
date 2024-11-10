import pathlib
import random

# 이 파일과 동일한 폴더에 oj.py가 있어야 합니다.
# oj.py 주소: https://gist.github.com/hepheir/c4c6326c48b1af344196c1d115d4eca1

from oj import Problem


BASE_DIR = pathlib.Path(__file__).parent.resolve()

SOLUTION_FILE = BASE_DIR/"solution.py"
TESTCASE_DIR = BASE_DIR/"testcase"
TESTCASE_ZIP_FILE = BASE_DIR/"apt.zip"


###############################################################
# 문제 생성과 관련된 상수, 유틸리티 함수 정의
###############################################################

# random 모듈의 함수들로 생성되는 값이 일관성을 갖도록 시드 설정
random.seed(0)

MIN_N = 1
MAX_N = int(1e4)

MIN_K = 1
MAX_K = int(1e6)

MIN_H = 0
MAX_H = int(2e4)

MAX_NAME_LENGTH = 20


RANDOM_NAMES = ["LillieLeonard", "RicardoPhelps", "LaneyClements", "FisherBarron", "AnyaFox", "AntonioRush", "MaleahLarsen", "BrycenGoodwin", "ShilohChambers", "OrionMeza", "RosaOsborne", "AugustusHunt", "GenevieveBecker", "LawsonGrant", "AlainaSpence", "CillianChoi", "KarlaBernal", "EithanPalacios", "BriaCallahan", "QuintonAllison", "ChelseaBowman", "FranciscoBuck", "LiviaWard", "JamesonWheeler", "SydneyRaymond", "MauriceAdkins", "EmeliaMathews", "JamirManning", "JenniferPacheco", "ErikDavid", "HayleeVelasquez", "SullivanCharles", "JennaBarnes", "DamianWang", "KailaniJimenez", "SilasGraves", "ElleAcosta", "JensenDouglas", "AniyahCallahan", "QuintonSmith", "OliviaPittman", "ValentinoWilkins", "AmaliaHopkins", "AliJames", "QuinnBryan", "JaxtynKane", "ElliannaHart", "JoelReilly", "ToriWheeler", "KennethPittman", "MarieNielsen", "TruSmith", "OliviaLloyd", "ZaireSweeney", "YaraJackson", "SebastianStephenson", "KhaleesiGuerrero", "BryceMullins", "MaliyahTucker", "IvanMay", "AdrianaBurton", "ZanderRoss", "PeytonConley", "MarvinMcCarty", "HaloSierra", "DaytonMatthews", "LilaHubbard", "ForrestBryant", "ParkerChristensen", "GregoryIbarra", "MadilynnZamora", "QuentinBenitez", "AlizaNorman", "AzielVo", "ArtemisPeck", "YousefQuintana", "KeniaMedina", "GeorgePena", "RachelFitzgerald", "PeytonBrewer", "TheaBenjamin", "KyroAvila", "AmiyahBurgess", "KoltonMatthews", "LilaGentry", "MagnusShaw", "EmersynBlevins", "AviAvery", "MeghanMoyer", "AhmirBoone", "MariamTucker", "IvanVaughn", "ReignSmall", "RudyPortillo", "NathalieHarvey", "CaydenCortes", "LeaMcCarthy", "DevinBean", "JenesisPeterson", "SantiagoLewis", "ElliePerkins", "KyrieFriedman", "AspynPetersen", "SamsonDuncan", "EliseBenson", "DesmondSnow", "AlexiaCuevas", "BreckenWall", "JaydaBarajas", "BrennanMendoza", "CoraCalderon", "OakleyHowell", "MckennaDyer", "AtreusBrandt", "LorettaNash", "ChandlerHester", "ZendayaHawkins", "VictorRoy", "SavannaStanley", "ManuelBranch", "LuisaBarron", "DustinHarmon", "MarenMacias", "MosheDouglas", "AniyahWiggins", "AzariahWright", "LilyWolf", "JaseDuncan", "EliseVaughan",
                "CastielBean", "JenesisMedina", "GeorgeBell", "MelodyMitchell", "JaxonEaton", "MileyLam", "BodieBrooks", "AutumnChristensen", "GregoryWatson", "HaileyAlvarez", "XavierBuchanan", "MaryamBerger", "ByronClay", "AlianaCano", "TerryMathis", "AnneMontes", "DarrenHubbard", "RosieNash", "ChandlerWu", "LianaEnglish", "JuniorFarley", "WrenleyCasey", "ArmandoBooth", "ZariyahHolloway", "SuttonKeith", "ElyseMendez", "ArthurGriffin", "CharlieWiley", "MathewNielsen", "ViennaRamsey", "LucianoBrowning", "PrincessJones", "WilliamCaldwell", "EvelynnLiu", "PedroKing", "VictoriaGalvan", "KingsleyChandler", "VivianaHuerta", "DouglasBenjamin", "JiannaPorter", "RhettPatel", "MadelineShah", "ZainBrowning", "PrincessWhitaker", "KeithHarding", "AniyaPerez", "OwenMahoney", "PromiseThornton", "MalikEspinoza", "LucilleMunoz", "JustinHickman", "ScarletteWright", "GraysonPeterson", "CarolineBallard", "KenzoMoses", "KarterPalmer", "TheoHebert", "KyleighPugh", "JudsonHunter", "KhloePowell", "BennettCortes", "LeaBlackwell", "MarcellusLewis", "EllieGreen", "AnthonySellers", "MercyHorn", "WilsonCoffey", "PaolaBarr", "HarleyLester", "AveriAvery", "JakariCorrea", "ValeryVillegas", "ClydeBaxter", "LaraDillon", "AlvinVasquez", "RoseKhan", "KendrickBradshaw", "BerkleyHuang", "AyaanBlackburn", "FridaBarry", "EmeryFitzpatrick", "AnnabellaAshley", "KylenAlvarez", "LeilaniEspinosa", "KhalidHamilton", "MackenzieGallegos", "JonasTodd", "ZariahFarley", "GraysenReynolds", "IsabelleLu", "DuncanCorona", "MariannaCampbell", "ChristopherRosas", "JoelleAcosta", "JensenLandry", "BrynleighCruz", "RyanYu", "NavyCortes", "BanksEverett", "NoahGross", "QuinnLucero", "IlaFord", "LuisStrickland", "NiaWells", "MaxEsquivel", "JayleeBecker", "LawsonVilla", "JohannaRobles", "OttoSolis", "MiracleLi", "JorgeBarr", "NoemiSanford", "TruettMassey", "ClementinePotts", "AlfredBenjamin", "JiannaJefferson", "RaylanCopeland", "DayanaSalgado", "TraceRoy", "SavannaMaldonado", "JavierONeill", "KennaRosas", "RemiCannon", "NoaBarrett", "AngeloBernal", "EmmelineLopez", "MichaelMcKee", "KoriLove", "JeffreyAli"]


def generate_more_names():
    global RANDOM_NAMES
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    RANDOM_NAMES = set(RANDOM_NAMES)
    while len(RANDOM_NAMES) < (2*MAX_N):
        namelen = random.randint(1, MAX_NAME_LENGTH)
        name = "".join(random.choices(ALPHABETS, k=namelen))
        RANDOM_NAMES.add(name)
    RANDOM_NAMES = sorted(RANDOM_NAMES)


def validate_names():
    def validate_name(name: str) -> bool:
        # 이름이 문제의 조건과 일치하는지 검사
        assert 1 <= len(name) <= MAX_NAME_LENGTH
        assert all(c.isalpha() for c in name)
        return True
    assert all(validate_name(name) for name in RANDOM_NAMES)


generate_more_names()
validate_names()


def get_n_random_names(n: int) -> list[str]:
    assert n <= len(RANDOM_NAMES)
    sample = random.sample(RANDOM_NAMES, n)
    random.shuffle(sample)
    return sample


def get_n_unique_random_ints(n: int, lo: int, hi: int) -> list[int]:
    assert lo <= hi
    sample = random.sample(range(lo, hi+1), n)
    random.shuffle(sample)
    return sample


###############################################################
# 테스트케이스 생성
###############################################################

problem = Problem(answer_file=SOLUTION_FILE)


# 예제 테스트케이스 생성

with problem.testcase("1") as sys:
    lines = [
        "3 4",
        "SooMoong 343 389",
        "DongJoo 361 423",
        "NamJu 374 407",
    ]
    sys.stdin.write("\n".join(lines))


with problem.testcase("2") as sys:
    lines = [
        "3 10",
        "SooMoong 343 389",
        "DongJoo 361 423",
        "NamJu 374 407",
    ]
    sys.stdin.write("\n".join(lines))


# 랜덤 테스트케이스 생성

with problem.testcase("3") as sys:
    N, K = 3, 4
    sys.stdin.write(f"{N} {K}\n")
    name_gen = iter(get_n_random_names(N))
    height_gen = iter(get_n_unique_random_ints(2*N, MIN_H, MAX_H))
    for n in range(N):
        sys.stdin.write(f"{next(name_gen)} {next(height_gen)} {next(height_gen)}\n")


for i in range(4, 11):
    with problem.testcase(str(i)) as sys:
        N, K = random.randint(MIN_N, MAX_N), random.randint(MIN_K, MAX_K)
        sys.stdin.write(f"{N} {K}\n")
        name_gen = iter(get_n_random_names(N))
        height_gen = iter(get_n_unique_random_ints(2*N, MIN_H, MAX_H))
        for n in range(N):
            sys.stdin.write(f"{next(name_gen)} {next(height_gen)} {next(height_gen)}\n")


# 생성한 테스트케이스 저장

problem.save(zipname=TESTCASE_ZIP_FILE, dirname=TESTCASE_DIR)
