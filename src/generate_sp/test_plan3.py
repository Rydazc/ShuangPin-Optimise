#!/usr/bin/python3

import math
import matplotlib.pyplot as plt
import numpy as np

pinyin_freq_list = [
    ('shi', -0.3236428117968411), ('yi', -0.4097843561088526),
    ('ji', -0.47802880934740943), ('yu', -0.582742618644487),
    ('zhi', -0.6603937834402575), ('qi', -0.8591694113303111),
    ('fu', -0.8844634687514968), ('wei', -0.8957818231203194),
    ('li', -0.9189229722927724), ('jian', -0.9626538564971686),
    ('you', -0.9791164813006594), ('yan', -0.9932577972815763),
    ('xi', -1.004164722579965), ('wu', -1.0683556997784538),
    ('de', -1.0915777225777987), ('shu', -1.175714320577575),
    ('xiang', -1.1827834879880463), ('jie', -1.1869209842779356),
    ('zhu', -1.1923793313934046), ('xian', -1.2219669053086513),
    ('di', -1.257604216471389), ('he', -1.272478432985853),
    ('yuan', -1.2834983600669065), ('jing', -1.3127171595661682),
    ('jiao', -1.346402908073335), ('jin', -1.3550750665157112),
    ('bi', -1.3729173682911653), ('ju', -1.3750502813393495),
    ('hui', -1.379686888356587), ('jia', -1.385479747192456),
    ('qian', -1.3985131820800323), ('ye', -1.428424919013606),
    ('ba', -1.4330124233893946), ('yao', -1.4351063944944162),
    ('xiao', -1.4389615544262861), ('mei', -1.4604586708597047),
    ('ge', -1.472518024324501), ('jiu', -1.4730662808374484),
    ('si', -1.4807769159501998), ('ying', -1.5010833361998959),
    ('xie', -1.5114317514164877), ('ta', -1.5224110799559658),
    ('gu', -1.5301845821286804), ('yin', -1.5333975344307325),
    ('zhe', -1.552106452307911), ('zi', -1.5563233685771571),
    ('hu', -1.5601349762912957), ('ke', -1.5732754408557181),
    ('xing', -1.588891001954462), ('zai', -1.5936622676813261),
    ('qu', -1.594219163575524), ('wan', -1.6136619654341553),
    ('dao', -1.6211132805463797), ('lu', -1.6223395174939115),
    ('bei', -1.64509959201423), ('mo', -1.6551931004653853),
    ('qing', -1.6577964073055826), ('ya', -1.6590670133439644),
    ('bao', -1.6607719463817006), ('zhen', -1.6679070495149795),
    ('zhong', -1.6730703115690295), ('ling', -1.6803420147258854),
    ('cheng', -1.6803946135483236), ('ni', -1.6858701128169018),
    ('jiang', -1.687400789637877), ('xu', -1.6880290674135068),
    ('wo', -1.6892198470159543), ('ma', -1.6974162555689583),
    ('ban', -1.7040807918610918), ('le', -1.7075851683031102),
    ('tong', -1.7088258249587625), ('zheng', -1.7115144588378794),
    ('du', -1.7135946747102901), ('yang', -1.719374600252068),
    ('chi', -1.719552695117224), ('han', -1.7203127817516517),
    ('fan', -1.7227161379084373), ('shen', -1.7235838900177756),
    ('bu', -1.7261233527815059), ('dan', -1.7371093361615464),
    ('zhang', -1.7504952423526328), ('feng', -1.7762042412802115),
    ('chu', -1.7827210495777284), ('bo', -1.7832292363367157),
    ('fei', -1.7963171254171986), ('lian', -1.7993039313834185),
    ('yue', -1.7993592976584087), ('chang', -1.800567771016463),
    ('gong', -1.8023514152807765), ('er', -1.806329997055642),
    ('shan', -1.8094507014683423), ('wang', -1.8164766968489647),
    ('zhao', -1.817084408485215), ('tan', -1.819276565611733),
    ('hao', -1.828731101685714), ('na', -1.8298061374927759),
    ('sheng', -1.8339660538640457), ('xin', -1.8380491104152339),
    ('huo', -1.8393001247756493), ('bian', -1.8396667589433335),
    ('hua', -1.849620662248006), ('dian', -1.8707348663410208),
    ('guan', -1.870771055235236), ('e', -1.871560300847485),
    ('shou', -1.8726737656107397), ('pi', -1.884039540938024),
    ('da', -1.8844414973458439), ('xia', -1.8945085978647915),
    ('dai', -1.8982726399258314), ('liu', -1.9082535296076595),
    ('zuo', -1.9091250991491446), ('ai', -1.9117286642027072),
    ('mi', -1.912050811387599), ('ci', -1.9120566469326625),
    ('gui', -1.9264179288836245), ('liang', -1.9355655019894042),
    ('mu', -1.9356964609929754), ('ren', -1.9359995972438326),
    ('yong', -1.9371384933232898), ('cai', -1.9395009189779664),
    ('an', -1.9463032369464912), ('wen', -1.9488866130860563),
    ('gan', -1.9601453325382343), ('dou', -1.969031825255717),
    ('shang', -1.9877676918679488), ('bing', -1.9921449205779462),
    ('chen', -1.9946151076062284), ('fang', -2.012004721315372),
    ('ding', -2.015015947881361), ('tang', -2.018082021862052),
    ('xun', -2.019683477773229), ('lv', -2.027070124205216),
    ('ting', -2.030339100543935), ('fen', -2.0324788549655284),
    ('yun', -2.034372233155917), ('huan', -2.0428915358895128),
    ('guo', -2.050829028338414), ('ti', -2.058662862722362),
    ('hai', -2.061027843023628), ('dong', -2.0651243994127992),
    ('zhou', -2.0670121157050296), ('quan', -2.067484476991058),
    ('hou', -2.068252079287798), ('lan', -2.070121963198894),
    ('zhan', -2.0718051674835327), ('tu', -2.0742442560863346),
    ('cha', -2.0902684268342995), ('sha', -2.099370244685858),
    ('su', -2.0998452090789774), ('tai', -2.106625804978554),
    ('qiao', -2.106982169798202), ('gao', -2.1138972200645694),
    ('mao', -2.124518654209799), ('ru', -2.1245313273389943),
    ('nian', -2.128408081645415), ('luo', -2.133350834656905),
    ('duo', -2.13446544186176), ('huang', -2.1463077258648857),
    ('lei', -2.147284243241118), ('lin', -2.149501896920114),
    ('ming', -2.1617745413400664), ('qin', -2.1656697048819997),
    ('deng', -2.1659554741105596), ('she', -2.169138000410183),
    ('jun', -2.179502081506136), ('qiang', -2.1853565420446954),
    ('xuan', -2.189223173932227), ('pu', -2.1940456342787527),
    ('sui', -2.1955585215632056), ('hong', -2.201681148647331),
    ('tao', -2.204274104284466), ('a', -2.206468888593252),
    ('tian', -2.2074991663083816), ('bai', -2.211481749838994),
    ('ping', -2.2211686081695543), ('kan', -2.2237405302139357),
    ('meng', -2.2275237462749473), ('shao', -2.229062290328556),
    ('liao', -2.2359056082924753), ('gou', -2.2372204964939035),
    ('zao', -2.2377716551744307), ('jue', -2.2420533760973997),
    ('qiu', -2.243777378565762), ('suo', -2.2507097754576924),
    ('xiu', -2.2567060778295702), ('chao', -2.2645064068212615),
    ('xue', -2.2733597471787856), ('lao', -2.2773805001629266),
    ('tuo', -2.289173430585889), ('song', -2.3367631865102276),
    ('dui', -2.3435997953396757), ('chan', -2.343799635419027),
    ('chou', -2.348472671807382), ('man', -2.352427749207405),
    ('chuan', -2.362199447745354), ('la', -2.3859165764130577),
    ('fa', -2.3892145843523385), ('peng', -2.3965620695768894),
    ('shuo', -2.3978351070883757), ('shui', -2.4056051371633105),
    ('lai', -2.406631076236352), ('dang', -2.4075673503106856),
    ('zhuo', -2.4080570200672975), ('zhuang', -2.4174820471956604),
    ('gang', -2.4181240956595667), ('cong', -2.4268354209145944),
    ('zui', -2.4291442764384117), ('mai', -2.429427738580963),
    ('ku', -2.4342276614545244), ('nan', -2.4373746133441783),
    ('po', -2.4389489627587055), ('zha', -2.4507357838142996),
    ('lou', -2.455254131737875), ('bang', -2.4562000187084942),
    ('pan', -2.4669880300199094), ('mian', -2.4703263323563456),
    ('zu', -2.476806672260866), ('hen', -2.4812473269001427),
    ('miao', -2.483092355401783), ('men', -2.488844610063393),
    ('pei', -2.492397754606142), ('ao', -2.4953631942069907),
    ('zhuan', -2.499280969061939), ('gai', -2.5042010731728785),
    ('diao', -2.505946379918723), ('que', -2.508876697032547),
    ('long', -2.5091008600014213), ('kui', -2.509857850057286),
    ('tiao', -2.527374630519274), ('lang', -2.5284354429106455),
    ('rong', -2.528707097003213), ('chong', -2.5366494197085623),
    ('biao', -2.557443302196749), ('pao', -2.565635416927703),
    ('pian', -2.573376710151852), ('can', -2.5751320336905077),
    ('geng', -2.5889909603115244), ('pai', -2.6014294568988614),
    ('dun', -2.612975342539538), ('tou', -2.617592292694174),
    ('gua', -2.6244247504030542), ('chun', -2.6266095032458066),
    ('zong', -2.639888223563171), ('wa', -2.644682700531019),
    ('pa', -2.654551471225258), ('duan', -2.658752331444928),
    ('ou', -2.6633976667908392), ('juan', -2.6642392384286606),
    ('hun', -2.66568709942823), ('ze', -2.6701987393787934),
    ('san', -2.6722369262193255), ('qie', -2.676985439224589),
    ('xiong', -2.6801115463377854), ('tie', -2.6814427388307904),
    ('kuang', -2.6882833547059963), ('pin', -2.694809423290526),
    ('zhai', -2.6988350123606746), ('cao', -2.6989443528269),
    ('piao', -2.6991328421569305), ('die', -2.720069273355312),
    ('min', -2.749095935443263), ('che', -2.757636776960488),
    ('kai', -2.7609387329361814), ('ben', -2.773220373679095),
    ('tui', -2.794213896545459), ('kao', -2.796190456842422),
    ('lie', -2.8020492060974025), ('ne', -2.804068367265582),
    ('gen', -2.806093676480007), ('kuai', -2.8073910160754063),
    ('cui', -2.814914194350316), ('lun', -2.8169958836000077),
    ('cuo', -2.8181339849726696), ('rang', -2.845553839236753),
    ('guang', -2.871312413513712), ('zan', -2.875418625391464),
    ('heng', -2.878549150325137), ('nao', -2.879444743192407),
    ('kou', -2.8845070549282372), ('zou', -2.9138385642085884),
    ('kong', -2.9179915467843403), ('niu', -2.9226989768725296),
    ('nong', -2.9247248013016445), ('chuang', -2.953946542797964),
    ('nie', -2.9787927703301276), ('nai', -2.9834453328735475),
    ('kang', -2.98357917193754), ('ce', -2.9927914338501305),
    ('ran', -2.994878432913161), ('mang', -3.0121005950435036),
    ('bin', -3.01263686432542), ('za', -3.01272513878302),
    ('cun', -3.0138089976795777), ('luan', -3.0254718201140913),
    ('shuai', -3.0403264822811815), ('neng', -3.049),
    ('zhui', -3.0518948110172026), ('o', -3.0751954646311983),
    ('cu', -3.076716642265938), ('chui', -3.081041809294336),
    ('huai', -3.0956783028554278), ('bie', -3.102803844297958),
    ('pang', -3.104991836930151), ('mou', -3.113868121159124),
    ('sun', -3.137710641357928), ('gei', -3.141846906337033),
    ('sa', -3.1422900039919965), ('se', -3.151879599579434),
    ('cang', -3.15527642317267), ('rou', -3.160156591046943),
    ('ning', -3.1668824534382054), ('shuang', -3.167243881379577),
    ('niao', -3.172476700979319), ('suan', -3.1790502867721213),
    ('en', -3.180682197832223), ('zeng', -3.182432655762258),
    ('kun', -3.195011775075795), ('ruo', -3.2033985298509386), ('ri', -3.2113),
    ('rui', -3.2457973170074665), ('beng', -3.2627688236736914),
    ('wai', -3.2773906414262277), ('teng', -3.2822823164852926),
    ('leng', -3.28437010562366), ('qun', -3.28759617671023),
    ('ceng', -3.290260110880601), ('nu', -3.314336114585746),
    ('sao', -3.3160396749979264), ('sou', -3.31775429092946),
    ('zang', -3.326217026137011), ('chai', -3.329685400840416),
    ('nei', -3.331801940372617), ('hei', -3.3456574235585985),
    ('qiong', -3.3497745949004507), ('me', -3.360258648015187),
    ('hang', -3.364451359521015), ('guai', -3.3660772199524964),
    ('sai', -3.3741335552855514), ('kua', -3.406224461948147),
    ('nin', -3.4542191058808065), ('ga', -3.465220459114904),
    ('nuo', -3.4738517986968453), ('rao', -3.478958083182449),
    ('tun', -3.486425845767178), ('ha', -3.495560974565649),
    ('ka', -3.5078887330855677), ('r', -3.5087), ('re', -3.5178948285624734),
    ('nv', -3.5269300424312457), ('gun', -3.567309788580371),
    ('kuan', -3.56978072549944), ('shun', -3.590706387115526),
    ('te', -3.5978077488132603), ('zuan', -3.602836039590171),
    ('sang', -3.604383809387909), ('zhua', -3.6050266174180763),
    ('ken', -3.64576380236204), ('shua', -3.6506212141332255),
    ('mie', -3.6649978368734843), ('kuo', -3.7438691537446678),
    ('cuan', -3.760463218211035), ('qia', -3.7922967073404483),
    ('reng', -3.798223469182788), ('tuan', -3.8083241693365197),
    ('niang', -3.8142791152249655), ('pen', -3.851723360986209),
    ('zun', -3.862080313966785), ('ruan', -3.894318241108033),
    ('zhun', -3.9455224620521383), ('lve', -3.9968249448288153),
    ('fo', -4.00888676608172), ('ng', -4.023654676423939),
    ('n', -4.023654676423939), ('weng', -4.025911457359591),
    ('keng', -4.0274426949675055), ('dei', -4.02874401572208),
    ('chuo', -4.037680039934101), ('nen', -4.045368567936544),
    ('shuan', -4.087813174300445), ('jiong', -4.094114401082424),
    ('shai', -4.116953773447544), ('ca', -4.125065661988082),
    ('nang', -4.148299300123272), ('yo', -4.161922458572623),
    ('chuai', -4.262730372779), ('cou', -4.283917506936045),
    ('shei', -4.289607001240464), ('run', -4.307952978003526),
    ('pie', -4.320838377913818), ('lo', -4.352463354188554),
    ('lia', -4.35728952024709), ('zen', -4.361487198355287),
    ('diu', -4.369306314200906), ('zei', -4.3996), ('fou', -4.476746101454727),
    ('nuan', -4.4901), ('sen', -4.4991), ('ang', -4.644787481510174),
    ('zhei', -4.65744229110894), ('seng', -4.6582),
    ('nve', -4.765740667847512), ('miu', -4.77438164870183),
    ('zhuai', -4.8427005927220605), ('cen', -4.89696936599128),
    ('pou', -4.940611697344074), ('ei', -4.9957), ('tei', -5.3016115661330865),
    ('dia', -5.3952), ('nou', -6.1404), ('m', -6.7878)
]
pinyin_list = [
    'shi', 'yi', 'ji', 'yu', 'zhi', 'qi', 'fu', 'wei', 'li', 'jian', 'you',
    'yan', 'xi', 'wu', 'de', 'shu', 'xiang', 'jie', 'zhu', 'xian', 'di', 'he',
    'yuan', 'jing', 'jiao', 'jin', 'bi', 'ju', 'hui', 'jia', 'qian', 'ye',
    'ba', 'yao', 'xiao', 'mei', 'ge', 'jiu', 'si', 'ying', 'xie', 'ta', 'gu',
    'yin', 'zhe', 'zi', 'hu', 'ke', 'xing', 'zai', 'qu', 'wan', 'dao', 'lu',
    'bei', 'mo', 'qing', 'ya', 'bao', 'zhen', 'zhong', 'ling', 'cheng', 'ni',
    'jiang', 'xu', 'wo', 'ma', 'ban', 'le', 'tong', 'zheng', 'du', 'yang',
    'chi', 'han', 'fan', 'shen', 'bu', 'dan', 'zhang', 'feng', 'chu', 'bo',
    'fei', 'lian', 'yue', 'chang', 'gong', 'er', 'shan', 'wang', 'zhao', 'tan',
    'hao', 'na', 'sheng', 'xin', 'huo', 'bian', 'hua', 'dian', 'guan', 'e',
    'shou', 'pi', 'da', 'xia', 'dai', 'liu', 'zuo', 'ai', 'mi', 'ci', 'gui',
    'liang', 'mu', 'ren', 'yong', 'cai', 'an', 'wen', 'gan', 'dou', 'shang',
    'bing', 'chen', 'fang', 'ding', 'tang', 'xun', 'lv', 'ting', 'fen', 'yun',
    'huan', 'guo', 'ti', 'hai', 'dong', 'zhou', 'quan', 'hou', 'lan', 'zhan',
    'tu', 'cha', 'sha', 'su', 'tai', 'qiao', 'gao', 'mao', 'ru', 'nian', 'luo',
    'duo', 'huang', 'lei', 'lin', 'ming', 'qin', 'deng', 'she', 'jun', 'qiang',
    'xuan', 'pu', 'sui', 'hong', 'tao', 'a', 'tian', 'bai', 'ping', 'kan',
    'meng', 'shao', 'liao', 'gou', 'zao', 'jue', 'qiu', 'suo', 'xiu', 'chao',
    'xue', 'lao', 'tuo', 'song', 'dui', 'chan', 'chou', 'man', 'chuan', 'la',
    'fa', 'peng', 'shuo', 'shui', 'lai', 'dang', 'zhuo', 'zhuang', 'gang',
    'cong', 'zui', 'mai', 'ku', 'nan', 'po', 'zha', 'lou', 'bang', 'pan',
    'mian', 'zu', 'hen', 'miao', 'men', 'pei', 'ao', 'zhuan', 'gai', 'diao',
    'que', 'long', 'kui', 'tiao', 'lang', 'rong', 'chong', 'biao', 'pao',
    'pian', 'can', 'geng', 'pai', 'dun', 'tou', 'gua', 'chun', 'zong', 'wa',
    'pa', 'duan', 'ou', 'juan', 'hun', 'ze', 'san', 'qie', 'xiong', 'tie',
    'kuang', 'pin', 'zhai', 'cao', 'piao', 'die', 'min', 'che', 'kai', 'ben',
    'tui', 'kao', 'lie', 'ne', 'gen', 'kuai', 'cui', 'lun', 'cuo', 'rang',
    'guang', 'zan', 'heng', 'nao', 'kou', 'zou', 'kong', 'niu', 'nong',
    'chuang', 'nie', 'nai', 'kang', 'ce', 'ran', 'mang', 'bin', 'za', 'cun',
    'luan', 'shuai', 'neng', 'zhui', 'o', 'cu', 'chui', 'huai', 'bie', 'pang',
    'mou', 'sun', 'gei', 'sa', 'se', 'cang', 'rou', 'ning', 'shuang', 'niao',
    'suan', 'en', 'zeng', 'kun', 'ruo', 'ri', 'rui', 'beng', 'wai', 'teng',
    'leng', 'qun', 'ceng', 'nu', 'sao', 'sou', 'zang', 'chai', 'nei', 'hei',
    'qiong', 'me', 'hang', 'guai', 'sai', 'kua', 'nin', 'ga', 'nuo', 'rao',
    'tun', 'ha', 'ka', 'r', 're', 'nv', 'gun', 'kuan', 'shun', 'te', 'zuan',
    'sang', 'zhua', 'ken', 'shua', 'mie', 'kuo', 'cuan', 'qia', 'reng', 'tuan',
    'niang', 'pen', 'zun', 'ruan', 'zhun', 'lve', 'fo', 'ng', 'n', 'weng',
    'keng', 'dei', 'chuo', 'nen', 'shuan', 'jiong', 'shai', 'ca', 'nang', 'yo',
    'chuai', 'cou', 'shei', 'run', 'pie', 'lo', 'lia', 'zen', 'diu', 'zei',
    'fou', 'nuan', 'sen', 'ang', 'zhei', 'seng', 'nve', 'miu', 'zhuai', 'cen',
    'pou', 'ei', 'tei', 'dia', 'nou', 'm'
]

sheng_list = [
    'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh',
    'ch', 'sh', 'r', 'z', 'c', 's', 'y', 'w'
]
yun_list = [
    'in', 'ian', 'iao', 'a', 'g', 'uo', 'ou', 'ui', 'ia', 'uang', 'ao', 'eng',
    'e', 'ang', 'o', 'ong', 'ei', 'ua', 'uan', 'un', 'i', 'u', 'ie', 've', 'v',
    'an', 'iong', 'iang', 'iu', 'ue', 'uai', 'er', 'en', 'ai', 'ing'
]

yun_stable_list = [
    ['iu'], ['ei'], ['e'], ['uan'], ['ue', 've'], ['un'], ['u'], ['i'], ['uo', 'o'], 
    ['ie'], ['a'], ['iong', 'ong'], ['ai'], ['en'], ['eng'], ['ang'], ['an'], ['ing', 'uai'], 
    ['iang', 'uang'], ['ou'], ['ia', 'ua'], ['ao'], ['v', 'ui'], ['in'], ['iao'], ['ian']
]


button_list = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm'
]


keys_cycle_str = "jfkdlsghrtynmbwpqcxz"
yun_cycle_list = [
    ['iu'], ['ei'], ['uan'], ['ue', 've'], ['un'],
    ['ie'], ['iong', 'ong'], ['ai'], ['en'], ['eng'], ['ang'], ['an'], ['ing', 'uai'], 
    ['iang', 'uang'], ['ou'], ['ia', 'ua'], ['ao'], ['in'], ['iao'], ['ian']
]


mapping_dict = {
    "sheng": {
        "b": "b",
        "p": "p",
        "m": "m",
        "f": "f",
        "d": "d",
        "t": "t",
        "n": "n",
        "l": "l",
        "g": "g",
        "k": "k",
        "h": "h",
        "j": "j",
        "q": "q",
        "x": "x",
        "r": "r",
        "z": "z",
        "c": "c",
        "s": "s",
        "y": "y",
        "w": "w",
        "zh": "v",
        "ch": "i",
        "sh": "u"
    },
    "yun": {
        "a": "a", 
        "o": "o", 
        "uo": "o", 
        "e": "e", 
        "i": "i", 
        "u": "u", 
        "v": "v", 
        "ui": "v"
    }
}

# keystroke_grade_dict = {
#     'qq': 8,
#     'qw': 7, 
#     'qe': 7, 
#     'qr': 7,
#     'qt': 7,
#     'qy': 9

# }

# keyboard_finger_dict = {
#     'left_small': 'qaz', 
#     'left_noname': 'wsx', 
#     'left_middle': 'edc', 
#     'left_eat': 'rfvtgb', 
#     'right_eat': 'yhnujm', 
#     'right_middle': 'ik', 
#     'right_noname': 'ol', 
#     'right_small': 'p'
# }

#　key source of keys [hand_flag, finger_flag, line_flag]
# use the different flag calulate the source of current source, to made the source could satisfy the rating system



"""desciption of classification dict
lift hand: 1
right hand: 0

index finger: 1000
middle finger: 100
ring finger: 10
little finger: 1

down line: 1
middle line: 100
up line:  10

"""
key_classification_dict = {

    "q": (1, 1, 100), 
    "w": (1, 10, 100),
    "e": (1, 100, 100), 
    "r": (1, 1000, 100), 
    "t": (1, 1000, 100), 
    "y": (0, 1000, 100), 
    "u": (0, 1000, 100), 
    "i": (0, 100, 100), 
    "o": (0, 10, 100), 
    "p": (0, 1, 100), 
    "a": (1, 1, 10), 
    "s": (1, 10, 10), 
    "d": (1, 100, 10), 
    "f": (1, 1000, 10), 
    "g": (1, 1000, 10), 
    "h": (0, 1000, 10), 
    "j": (0, 1000, 10), 
    "k": (0, 100, 10), 
    "l": (0, 10, 10), 
    "z": (1, 1, 1), 
    "x": (1, 10, 1), 
    "c": (1, 100, 1), 
    "v": (1, 1000, 1), 
    "b": (1, 1000, 1), 
    "n": (0, 1000, 1), 
    "m": (0, 1000, 1)
    
}


def key_sequence_to_source(key_sequence:str) -> int:
    """example for key_sequence "qw", "er" ... 

    the idea of follow-up:
    add the single key source of the combination keys write bellow 
    the single key source just like :   0 level: j f 
                                        1 level: k d l s a
                                        2 level: g h u r t y 
                                        3 level: n m v b 
                                        4 level: i e o w p q 
                                        5 level: c x z 
    """

    if len(key_sequence) == 1:
        """once press key"""
        return 13
    elif len(key_sequence) == 2:
        """twice press key"""
        key1 = key_sequence[0]
        key2 = key_sequence[1]

        key1_class = key_classification_dict[key1]
        key2_class = key_classification_dict[key2]

        key1_hand = key_classification_dict[key1][0]
        key2_hand = key_classification_dict[key2][0]

        key1_finger = key_classification_dict[key1][1]
        key2_finger = key_classification_dict[key2][1]

        key1_line = key_classification_dict[key1][2]
        key2_line = key_classification_dict[key2][2]


        if key1_hand != key2_hand:
            """lift hand and right hand press the key"""
            if (key1_finger + key2_finger) % 10 == 0:
                """not use little finger"""
                return 12
            elif (key1_finger + key2_finger) % 10 == 1:
                """use once little finger"""
                return 11
            else:
                """use twice little finger"""
                return 10

        else:
            if key1 == key2: 
                """press the same keys twice"""
                return 9


            elif key1_class == key2_class:
                """index finger and neighbor key"""
                return 6


            elif key1_finger != key2_finger:
                """one-handed and different finger"""
                if (key1_finger + key2_finger) % 10 == 0:
                    """not use little finger"""
                    return 8
                else:
                    """use little finger"""
                    return 7

            else:
                """one-handed and same finger"""
                if key1_finger == key2_finger == 1000:
                    """index finger"""
                    if max(key1_line, key2_line) / min(key1_line, key2_line) == 10:
                        """neighbor key"""
                        return 6
                    else:
                        """not neighbor key """
                        return 2

                elif key1_finger == key2_finger == 100:
                    """middle finger"""
                    if max(key1_line, key2_line) / min(key1_line, key2_line) == 10:
                        """neighbor key"""
                        return 5
                    else:
                        """not neighbor key """
                        return 1

                elif key1_finger == key2_finger == 10:
                    """ring finger"""
                    if max(key1_line, key2_line) / min(key1_line, key2_line) == 10:
                        """neighbor key"""
                        return 4
                    else:
                        """not neighbor key """
                        return 0

                elif key1_finger == key2_finger == 1:
                    """little finger"""

                    if max(key1_line, key2_line) / min(key1_line, key2_line) == 10:
                        """neighbor key"""
                        return 3
                    else:
                        """not neighbor key """
                        return 0
    else:
        print("key input is outof range!")



def key_sequence_test():
    """the test of function 'key_sequence_to_source' """
    for button1 in button_list:
        source = key_sequence_to_source(button1)
        print(f"button:{button1}, source:{source}")

    for button2 in button_list:
        for button3 in button_list:
            source = key_sequence_to_source(button2+button3)
            print(f"button:{button2+button3}, source:{source}")





# 拼音拆分
def split_pinyin(pinyin: str) -> tuple:
    sheng2_tuple = ("zh", "ch", "sh")

    if pinyin.startswith(sheng2_tuple):
        return (pinyin[:2], pinyin[2:])
    elif pinyin.startswith(tuple(sheng_list)):
        return (pinyin[:1], pinyin[1:])
    else:
        return ("", pinyin)


# 根据拼音获取对应按键组合
def get_keys(pinyin: str, mapping_dict: dict) -> tuple:
    sheng_yun_tuple = split_pinyin(pinyin=pinyin)
    print(f"pinyin is {sheng_yun_tuple}")
    return (mapping_dict["sheng"][sheng_yun_tuple[0]],
            mapping_dict["yun"][sheng_yun_tuple[1]])


# 合规检测
def compliance_testing(keys_tuple: tuple):
    bad_keys = [("q", "z"), ("z", "q"), ("z", "w"), ("w", "z"), ("x", "q"),
                ("q", "x"), ("x", "w"), ("w", "x")]
    if keys_tuple in bad_keys:
        return False
    return True

"""
基于已给定声母排列的情况
/*
plan 1
从高使用率按键到低使用率按键开始遍历键盘, 之后从上到下赋值韵母, 计算所有使用当前赋值韵母时的使用率评分, 最后选出使用率最高的评分来使用
接着从韵母list中删除已使用的韵母, 遍历下一个键盘上的下一个按键和数据
 
*/


plan2 
基于已给定声母排列的情况
/*
通过拼音使用频率，计算得到韵母使用频率的数据
按照案件使用率从高到地排列韵母数据

*/




old plan
基于声母和韵母都未给定排列的情况
/*

对键盘拼音形式的遍历采用广度优先的搜索算法, 并每个节点进行一次拼写判定, 并把无用节点删除
判定条件：
1. 对该键位的拼音拼写遍历不在badkeys中, （且拼写分数高于中值）
2. 按键舒适度评分体系： 单键拼音 > 左右手分别击键(不使用小指 > 使用一次小指 > 使用两次小指)  > 同一按键重复两次 >单手不同击键(不使用小指 > 使用小指) > 食指相邻击键 > 中指相邻击键 > 
                    无名指相邻击键 > 小指相邻击键 > 食指跨按键击键 > 中指跨按键击键 
                    其他击键组合为0分
3. 适用汉字拼音频率评分： 根据pinyin_freq_list中的对数频率来评估, 分数越接近0, 分值越高，尽量使
                    频率高的拼音组合落在按键舒适度高的评分内
                        
 
 record: dictionary  记录按键到拼音的映射，每次记录后返回并且记录评分
    {'key', ['yun':str, point:float]}
 example:
    {'q':['in', '4.8']}
 */
 """





# function of data show 

def cal_weight_value(record=None) -> dict:
    if record.isinstance(dict):
        record_history = record
    else:
        record = {} 

    for button in button_list:
        if button not in record.keys():
        # 若该按键不在运算记录中，则结合已有记录计算
            for yun in yun_stable_list:
                if yun not in record.values():
                    pass 
                    # 计算韵母击键方式等分数
    

def cal_freq_list(freq_list):
    percent_freq_list = []
    for _ in freq_list:
        percent_freq_list.append((math.exp(float(_))))
    return percent_freq_list


# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 提前退出标志位
        swapped = False
        # 从0到n-i-1的范围内进行比较
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # 交换
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # 如果没有发生交换，说明数组已经是有序的
        if not swapped:
            break
    return arr


def data_show():
    freq_num_list = [num[1] for num in pinyin_freq_list]
    freq_num_list = bubble_sort(freq_num_list)
    freq_num_list_nolog = cal_freq_list(freq_num_list)
    freq_num = [_ for _ in range(len(freq_num_list))]

    # print(f'freq num list:{freq_num_list}')
    # print(f'type freq:{type(freq_num_list)}')
    # print(f'freq num:{freq_num}')
    # print(f'type freq num:{type(freq_num)}')

    plt.subplot(1, 2, 1)
    plt.plot(freq_num, freq_num_list_nolog, label="freq_num_of_orgin", color='r')
    plt.xlabel('x')
    plt.ylabel("freq")
    plt.title("freq orgin")
    plt.legend()
    plt.grid(True) 


    plt.subplot(1, 2, 2)
    plt.plot(freq_num, freq_num_list, label="freq_num_of_log", color='r')
    plt.xlabel('x')
    plt.ylabel("freq")
    plt.title("freq log")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()




def main():
    # result = split_pinyin("ao")
    # print(result)

    pass 

    # for key in pinyin_freq_list:
    #     split_pinyin_tuple = split_pinyin(key[0])
    #     print(split_pinyin_tuple)
        





if __name__ == '__main__':
    pass 
    # main()
    # sum_num = 0
    # freq_list = cal_freq_list(pinyin_freq_list)
    # print(freq_list)
    # for freq in freq_list:
    #     sum_num += freq[1]
    # print(sum_num)
    # data_show()
    key_sequence_test()



        
