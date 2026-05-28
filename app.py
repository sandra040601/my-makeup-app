import streamlit as st

# ==============================================================================
# 🗂️ 1. 膚質保養與底妝資料庫
# ==============================================================================
SKIN_DATABASE = {
    "oil": {
        "diagnosis": "【油性肌/痘痘肌學理診斷】\n臨床特徵為皮脂腺分泌過度旺盛。💡 產品挑選關鍵：應優先選擇含有『控油成分』或『酸類代謝成分』之清爽產品。",
        "1": {
            "makeup_remover": [{"name": "【妮維雅】雙層極淨卸妝水 $259", "reason": "清爽水狀質地，不含礦物油，溫和卸除不致痘。"}],
            "cleanser": [{"name": "【專科】超微米控油潔顏乳 $135", "reason": "含有宇治抹茶精華，微米泡沫能深入毛孔洗淨多餘油脂。"}],
            "essence": [{"name": "【Solone】補水噴霧 $119", "reason": "極輕透的水感補水，避開黏膩精華液，給予最純粹的表層保濕。"}],
            "cream": [{"name": "【惹我】清爽吸油蜜粉 $145", "reason": "大油肌夜間保養最後一步，薄拍一層乾粉吸附夜間油脂。"}],
            "makeup_base": [{"name": "【1028】超控油飾底乳 $299", "reason": "專為油肌設計，強力吸附油脂，延緩全臉暗沉。"}],
            "foundation": [{"name": "【Maybelline 媚比琳】反孔特霧粉底液 $420", "reason": "微米控油科技，打造頂級霧面啞光妝感。"}],
            "setting_powder": [{"name": "【惹我】清爽吸油蜜粉 $145", "reason": "極佳的乾粉吸油力，是油肌長效定妝的經典牌。"}]
        },
        "2": {
            "makeup_remover": [{"name": "【貝德瑪】平衡控油潔膚液 $450", "reason": "平衡皮脂分泌，溫和卸妝。"}],
            "cleanser": [{"name": "【Curel】控油保濕洗顏慕斯 $400", "reason": "洗去油脂的同時保護肌膚屏障。"}],
            "essence": [{"name": "【寶拉珍選】2%水楊酸精華液 $520", "reason": "代謝老廢角質，淨化毛孔。"}],
            "cream": [{"name": "【理膚寶水】毛孔緊緻控油保濕乳 $790", "reason": "有效抑制全天候的過度皮脂分泌。"}],
            "makeup_base": [{"name": "【Pony Effect】水透光控油妝前乳 $690", "reason": "控油兼具長效持妝效果。"}],
            "foundation": [{"name": "【KATE】零瑕肌密微霧粉底液 $540", "reason": "液態質地推開後化為微霧粉體。"}],
            "setting_powder": [{"name": "【innisfree】無油無慮礦物控油蜜粉 $250", "reason": "吸油力極強的開架明星控油蜜粉。"}]
        },
        "3": {
            "makeup_remover": [{"name": "【植村秀】黑米精萃潔顏油 $1200", "reason": "深入毛孔溶解黑頭與頑固彩妝。"}],
            "cleanser": [{"name": "【SK-II】全效活膚潔面乳 $1500", "reason": "溫和洗淨並維持肌膚細緻。"}],
            "essence": [{"name": "【理膚寶水】淨痘無瑕極效精華 DUO+ $950", "reason": "調理痘痘，預防瑕疵留痕。"}],
            "cream": [{"name": "【Kiehl's】冰河醣蛋白吸油水凝凍 $1600", "reason": "24小時零油光，膚感水嫩輕盈。"}],
            "makeup_base": [{"name": "【YSL】名模肌密光燦水凝露 $2150", "reason": "專櫃級水感控油打底。"}],
            "foundation": [{"name": "【雅詩蘭黛】粉持久完美持妝粉底 $2100", "reason": "油肌終極救星，越夜越美麗。"}],
            "setting_powder": [{"name": "【M·A·C】超持妝輕透濾鏡蜜粉 $1500", "reason": "煙霧般細緻粉體，徹底鎖死油光。"}]
        }
    },
    "dry": {
        "diagnosis": "【乾燥肌/缺水肌學理診斷】\n臨床特徵為角質層含水量屏障受損。💡 產品挑選關鍵：底妝必須優先選擇含有『高保濕因子』或『親膚性植物油』的潤澤型產品，避免卡粉脫屑。",
        "1": {
            "makeup_remover": [{"name": "【Biore 蜜妮】深層卸妝乳 $179", "reason": "乳狀質地減少摩擦，溫和卸妝不帶走乾肌珍貴油脂。"}],
            "cleanser": [{"name": "【肌研】極潤保濕洗面乳 $240", "reason": "添加高效玻尿酸，泡沫細緻，洗後肌膚水嫩不脫屑。"}],
            "essence": [{"name": "【肌研】極潤保濕化妝水 $440", "reason": "多重分子玻尿酸，是百元小資界最經典的高滲透補水神器。"}],
            "cream": [{"name": "【雪芙蘭】滋養霜 經典保濕 $79", "reason": "傳奇綿羊油配方，強效油脂在表皮形成嚴密鎖水薄膜。"}],
            "makeup_base": [{"name": "【Canmake】美人魚防曬啫喱 $300", "reason": "高達85%美容液成分，為乾燥肌底打好水潤基礎。"}],
            "foundation": [{"name": "【Media 媚點】粉嫩保濕礦物粉底霜 $280", "reason": "經典高滋潤霜狀質地，能完美服貼脫屑肌膚，不卡紋。"}],
            "setting_powder": [{"name": "【CEZANNE】抗UV保濕蜜粉餅 $290", "reason": "開架少見的保濕型蜜粉餅，細緻不乾燥，溫和定妝。"}]
        },
        "2": {
            "makeup_remover": [{"name": "【Curel】潤浸保濕卸妝凝露 $400", "reason": "溫和卸妝，守護肌膚神經醯胺。"}],
            "cleanser": [{"name": "【Cetaphil 舒特膚】溫和潔膚乳 $450", "reason": "不含皂鹼不緊繃，乾肌友善。"}],
            "essence": [{"name": "【雅詩蘭黛】特潤超導修護露(小棕瓶) $680", "reason": "夜間密集修護，鎖水功能強大。"}],
            "cream": [{"name": "【Curel】潤浸保濕深層乳霜 $720", "reason": "深層修護角質，緩解脫屑。"}],
            "makeup_base": [{"name": "【Pony Effect】水透光妝前防護乳 $690", "reason": "爆水神乳，保濕度極高不卡粉。"}],
            "foundation": [{"name": "【CLIO】柔霧光澤水感粉底液 $680", "reason": "兼具高保濕度與韓系奶油光。"}],
            "setting_powder": [{"name": "【Pony Effect】絕對持久定妝噴霧 $550", "reason": "以水霧代替乾粉定妝，鎖住肌膚水分。"}]
        },
        "3": {
            "makeup_remover": [{"name": "【EVE LOM】全能深層潔淨霜 $2500", "reason": "頂級乾肌養膚型卸妝。"}],
            "cleanser": [{"name": "【香奈兒】深海系列潔顏慕斯 $1650", "reason": "泡沫絲滑細緻，洗後完全不緊繃。"}],
            "essence": [{"name": "【蘭蔻】超未來肌因賦活露(小黑瓶) $3100", "reason": "嫩膚保濕，大幅改善乾燥粗糙。"}],
            "cream": [{"name": "【海洋拉娜】經典乳霜 $6800", "reason": "傳奇修護成分，強效封閉鎖水。"}],
            "makeup_base": [{"name": "【蘿拉蜜思】煥顏凝露(保濕型) $1500", "reason": "乾肌打底神物，瞬間撫平乾燥粗糙。"}],
            "foundation": [{"name": "【BOBBI BROWN】冬蟲夏草精華粉底 $2600", "reason": "頂級奢華養膚粉底，打造高級貴婦水光。"}],
            "setting_powder": [{"name": "【香奈兒】輕盈完美蜜粉 $2150", "reason": "專櫃頂級細緻乾粉，完全不乾澀脫皮。"}]
        }
    },
    "mix": {
        "diagnosis": "【混合肌學理診斷】\n面部皮脂腺分布不均，T字部位出油旺盛而雙頰乾燥緊繃。💡 產品挑選關鍵：底妝應選擇具有『水油平衡調節』能力的輕盈配方。",
        "1": {
            "makeup_remover": [{"name": "【Biore 蜜妮】溫和卸妝乳 $179", "reason": "均勻平衡全臉不同區域油脂狀態。"}],
            "cleanser": [{"name": "【Biore 蜜妮】溫和水嫩洗面乳 $115", "reason": "保濕成分留於雙頰，同時帶走 T 字皮脂。"}],
            "essence": [{"name": "【肌研】極潤保濕化妝水 $440", "reason": "單純玻尿酸補水，既不讓 T 字黏悶，又能滋潤雙頰。"}],
            "cream": [{"name": "【雪芙蘭】水潤凝霜 $129", "reason": "輕盈水凝霜質地，給予雙頰足夠鎖水力又不易悶長 T 字粉刺。"}],
            "makeup_base": [{"name": "【SOFINA 漾緁】控油瓷效妝前乳 $350", "reason": "適合局部塗抹在易出油的 T 字部位，達到完美分區控油。"}],
            "foundation": [{"name": "【Media 媚點】自然肌透持效粉底液 $330", "reason": "水潤好推不卡粉，對雙頰友善，且具有基本的 T 字抗汗力。"}],
            "setting_powder": [{"name": "【1028】超吸油蜜粉餅 $159", "reason": "分區定妝利器！重點按壓 T 字，雙頰輕輕帶過即可。"}]
        },
        "2": {
            "makeup_remover": [{"name": "【貝德瑪】舒敏潔膚液 $450", "reason": "溫和且質地清爽。"}],
            "cleanser": [{"name": "【Dr.Wu】玻尿酸保濕潔顏慕斯 $400", "reason": "水油平衡，洗後不緊繃。"}],
            "essence": [{"name": "【Origin 品木宣言】靈芝水 $520", "reason": "有效穩定混合肌不穩定的膚況。"}],
            "cream": [{"name": "【Kiehl's】冰河醣蛋白無油清爽凝凍 $1350", "reason": "補水不補油，適合混合肌夏天使用。"}],
            "makeup_base": [{"name": "【KATE】零瑕肌密持妝乳 $390", "reason": "平衡全臉水油分布。"}],
            "foundation": [{"name": "【Maybelline】反孔特霧粉底液 $420", "reason": "霧面質地，完美隱形 T 字毛孔。"}],
            "setting_powder": [{"name": "【1028】空氣定妝噴霧 $350", "reason": "水潤成膜，完美定住混合肌妝容。"}]
        },
        "3": {
            "makeup_remover": [{"name": "【植村秀】抹茶精萃潔顏油 $1500", "reason": "抗氧化且洗後膚感清爽。"}],
            "cleanser": [{"name": "【THREE】平衡潔膚油 $1450", "reason": "天然植物成分，調理肌膚平衡。"}],
            "essence": [{"name": "【SK-II】青春露 $3500", "reason": "全面調理、平衡水油分泌狀態。"}],
            "cream": [{"name": "【倩碧】水磁場72H保濕凝膠 $1500", "reason": "極致清爽的水凝膜質地。"}],
            "makeup_base": [{"name": "【植村秀】無極限保濕妝前乳 $1600", "reason": "保濕度足夠，且抗油抗汗不脫妝。"}],
            "foundation": [{"name": "【SHISEIDO 資生堂】超進化持久粉底液 $1800", "reason": "專利動態感應科技，面部遇油時更加持妝。"}],
            "setting_powder": [{"name": "【蘿拉蜜思】煥顏透明蜜粉 $1500", "reason": "專櫃經典蜜粉，完美柔焦且不易乾裂。"}]
        }
    },
    "sensitive": {
        "diagnosis": "【敏感肌/泛紅肌學理診斷】\n皮膚物理性與化學性屏障功能嚴重受損。💡 產品挑選關鍵：應嚴格遵循『極簡成分與無刺激學理』，底妝避開酒精、香料，優先選用純物理或礦物底妝。",
        "1": {
            "makeup_remover": [{"name": "【無印良品】敏感肌卸妝油 $290", "reason": "植物性橄欖油基底，配方極度單純。"}],
            "cleanser": [{"name": "【舒特膚】溫和潔膚乳 $299", "reason": "不含皂鹼、不含香料，超低刺激性。"}],
            "essence": [{"name": "【雅漾】舒護活泉水 $199", "reason": "完美鈣鎂比例，瞬間舒緩面部泛紅與刺痛。"}],
            "cream": [{"name": "【無印良品】敏感肌乳液 $250", "reason": "提供最基礎、單純的保濕鎖水，不給屏障帶來負擔。"}],
            "makeup_base": [{"name": "【無印良品】敏感肌防曬乳 $290", "reason": "純物理防曬配方，無酒精、無香料，極度溫和不刺痛。"}],
            "foundation": [{"name": "【Media 媚點】保濕礦物粉底霜 $280", "reason": "添加溫和礦物成分，對肌膚負擔小，不易引發敏感泛紅。"}],
            "setting_powder": [{"name": "【無印良品】敏感肌定妝蜜粉 $350", "reason": "極簡無刺激成分，輕盈定妝，不給受損皮膚帶來化學負擔。"}]
        },
        "2": {
            "makeup_remover": [{"name": "【理膚寶水】高效溫和卸妝水 $480", "reason": "含有極低摩擦舒敏因子。"}],
            "cleanser": [{"name": "【Curel】潤浸保濕洗顏慕斯 $480", "reason": "綿密慕斯減少雙手與泛紅肌的摩擦。"}],
            "essence": [{"name": "【理膚寶水】B5舒緩保濕修護精華 $950", "reason": "高濃度維生素B5加速屏障修復。"}],
            "cream": [{"name": "【理膚寶水】B5全面修復霜 $490", "reason": "萬用型的肌膚泛紅修復神霜。"}],
            "makeup_base": [{"name": "【Avene 雅漾】全效抗UV物理防曬乳 $790", "reason": "100%純物理防曬，敏弱肌安全。"}],
            "foundation": [{"name": "【d program 敏感話題】敏弱蜜粉餅 $1100", "reason": "專為舒緩低敏設計的溫和底妝。"}],
            "setting_powder": [{"name": "【理膚寶水】多容安舒緩修護噴霧 $750", "reason": "安心溫和的水霧定妝。"}]
        },
        "3": {
            "makeup_remover": [{"name": "【DARPHIN】全效舒緩卸妝乳 $1500", "reason": "經典粉紅療癒舒緩配方。"}],
            "cleanser": [{"name": "【THREE】平衡潔膚油 $1450", "reason": "天然植物成分，調理肌膚平衡。"}],
            "essence": [{"name": "【SK-II】青春露 $3500", "reason": "全面調理、平衡水油分泌狀態。"}],
            "cream": [{"name": "【倩碧】水磁場72H保濕凝膠 $1500", "reason": "極致清爽的水凝膜質地。"}],
            "makeup_base": [{"name": "【蘿拉蜜思】煥顏凝露(經典型) $1500", "reason": "明星全能打底，平衡面部水油結構。"}],
            "foundation": [{"name": "【SHISEIDO 資生堂】超進化持久粉底液 $1800", "reason": "專利動態感應科技，面部遇油時更加持妝。"}],
            "setting_powder": [{"name": "【蘿拉蜜思】煥顏透明蜜粉 $1500", "reason": "專櫃經典蜜粉，完美柔焦且不易乾裂。"}]
        }
    }
}

# ==============================================================================
# 💄 2. 風格彩妝獨立推薦資料庫
# ==============================================================================
MAKEUP_STYLE_DATABASE = {
    "1": { 
        "style_name": "韓系暖調大地色系妝容 (溫柔小清新)",
        "budget_data": {
            "1": {"eyeshadow": ["【1028】飛我莫屬限量眼彩盤 #杏影大地 $390"], "blusher": ["【Romand】勝過完美腮紅 $260"], "lipstick": ["【Romand】果汁水光唇釉 $280"]},
            "2": {"eyeshadow": ["【CLIO】璀璨星沙十色眼影盤 $680"], "blusher": ["【3CE】單色腮紅 $450"], "lipstick": ["【3CE】絲絨霧面唇釉 $490"]},
            "3": {"eyeshadow": ["【TOM FORD】高級定製四格眼盤 #03 $2600"], "blusher": ["【NARS】炫色腮紅 $1150"], "lipstick": ["【DIOR】癮誘唇膏 $1400"]}
        }
    },
    "2": { 
        "style_name": "溫柔玫瑰粉棕色系妝容 (約會招桃花)",
        "budget_data": {
            "1": {"eyeshadow": ["【heme】六色眼影盤 #玫瑰蜜桃 $299"], "blusher": ["【Canmake】花漾戀愛修容組 $390"], "lipstick": ["【Romand】果汁水光唇釉 $280"]},
            "2": {"eyeshadow": ["【3CE】九色眼影盤 #OVERTAKE $790"], "blusher": ["【Clinique 倩碧】小雛菊腮紅 $700"], "lipstick": ["【M·A·C】絲柔粉霧唇釉 $1050"]},
            "3": {"eyeshadow": ["【SUQQU】晶采盈緻眼彩盤 $2600"], "blusher": ["【CHANEL】圓形腮紅 $1500"], "lipstick": ["【Tom Ford】設計師唇膏 $1900"]}
        }
    },
    "3": { 
        "style_name": "輕歐美俐落消腫冷灰棕妝容 (高級感拉滿)",
        "budget_data": {
            "1": {"eyeshadow": ["【Solone】經典單色眼影自組盤 $250"], "blusher": ["【heme】純色腮紅 #04 $240"], "lipstick": ["【into you】唇泥 #EM23 $249"]},
            "2": {"eyeshadow": ["【KATE】色影迷棕眼影盤 $420"], "blusher": ["【3CE】單色腮紅 $450"], "lipstick": ["【MAC】時尚唇膏 #Taupe $800"]},
            "3": {"eyeshadow": ["【DIOR】經典五色眼影 #酷灰 $2500"], "blusher": ["【NARS】霧光修容餅 $1400"], "lipstick": ["【YSL】小黑條口紅 #314 $1450"]}
        }
    },
    "4": { 
        "style_name": "白開水偽素顏輕透妝容 (無心機純欲風)",
        "budget_data": {
            "1": {"eyeshadow": ["【Canmake】完美霧面眉影盤 $380"], "blusher": ["【heme】純色腮紅 #10 $240"], "lipstick": ["【CEZANNE】持久潤澤唇膏 $260"]},
            "2": {"eyeshadow": ["【Excel】裸色深邃眼影盤 #SR01 $535"], "blusher": ["【Clinique】小雛菊腮紅 #18 $700"], "lipstick": ["【OPERA】柔潤唇膏 #05 $380"]},
            "3": {"eyeshadow": ["【BOBBI BROWN】時尚奢華眼影 $1300"], "blusher": ["【SUQQU】晶采淨妍頰彩 $2100"], "lipstick": ["【CHANEL】COCO晶亮水唇膏 $1400"]}
        }
    }
}

# ==============================================================================
# 🔗 3. 護膚與妝容「線上教學影音」教程連結資料庫
# ==============================================================================
TUTORIAL_DATABASE = {
    "skincare": [
        {"title": "皮膚科莊盈彥醫師 - 基礎護膚學理與正確保養順序", "url": "https://www.youtube.com/results?search_query=%E8%8E%8A%E7%9B%88%E5%BD%A5+%E4%BF%9D%E9%A4%8A%E9%A0%86%E5%BA%8F"},
        {"title": "Dr. Ivan 6 - 混合肌與油肌分區控油穩膚防脫皮教學", "url": "https://www.youtube.com/results?search_query=Dr+Ivan+6+%E6%B7%B7%E5%90%88%E8%82%8C+%E4%BF%9D%E9%A4%8A"}
    ],
    "makeup_styles": {
        "1": {"title": "PONY - 韓系日常大地色消腫暖調妝容完整教學", "url": "https://www.youtube.com/results?search_query=PONY+%E9%9F%93%E7%B3%BB%E5%A4%A7%E5%9C%B0%E8%89%B2%E5%A6%9D%E5%AE%B9"},
        "2": {"title": "一枝南南 - 溫柔玫瑰粉棕色大面積腮紅招桃花約會妝", "url": "https://www.youtube.com/results?search_query=%E4%B8%80%E6%9E%9D%E5%8D%97%E5%8D%97+%E7%8E%AB%E7%91%B0%E7%B2%89%E6%A3%95%E5%A6%9D%E5%AE%B9"},
        "3": {"title": "Jcnana 蒨蒨 - 亞洲面孔消腫冷灰棕妝容與輕歐美結構修容術", "url": "https://www.youtube.com/results?search_query=Jcnana+%E5%86%B7%E7%81%B0%E6%A3%95%E5%A6%9D%E5%AE%B9"},
        "4": {"title": "鴨鴨 Makeup - 低粉感、低飽和無心機『白開水純欲妝』核心教學", "url": "https://www.youtube.com/results?search_query=%E9%B4%A8%E9%B4%A8+Makeup+%E5%85%AA%E9%96%8B%E6%B0%B4%E5%A6%9D%E5%AE%B9"}
    }
}

# ==============================================================================
# 🎨 4. Streamlit 網頁介面設計
# ==============================================================================
st.set_page_config(page_title="智慧美妝與護膚諮詢 App", page_icon="💄", layout="centered")

st.title("💄 智慧美妝與護膚諮詢 App")
st.write("一條龍搞定你的膚質診斷、分區挑選心法、客製化推薦與線上影音教程！")
st.markdown("---")

# 📥 使用者輸入區塊
st.header("🔍 第一步：請輸入您的個人條件")

skin_options = {"油性肌": "oil", "乾燥肌": "dry", "混合肌": "mix", "敏感肌": "sensitive"}
user_skin_label = st.selectbox("1. 您的主要膚質是什麼？", list(skin_options.keys()))
user_skin = skin_options[user_skin_label]

routine_options = {
    "🌙 深度夜間保養指南": "1",
    "✨ 韓系暖調大地色系妝容 (溫柔小清新)": "2",
    "🌹 溫柔玫瑰粉棕色系妝容 (約會招桃花)": "3",
    "🕶️ 輕歐美俐落消腫冷灰棕妝容 (高級感拉滿)": "4",
    "🥛 白開水偽素顏輕透妝容 (無心機純欲風)": "5"
}
user_routine_label = st.selectbox("2. 您今天想看保養還是化妝風格？", list(routine_options.keys()))
user_routine = routine_options[user_routine_label]

budget_options = {"💰 小資學生黨 (單品約 NT$300 左右)": "1", "💎 稍微有預算 (單品約 NT$300 - NT$800)": "2", "👑 精緻高級小奢華 (單品約 NT$800 以上)": "3"}
user_budget_label = st.selectbox("3. 您的預算級別？", list(budget_options.keys()))
user_budget = budget_options[user_budget_label]

# 🚀 觸發生成按鈕
if st.button("🚀 生成我的客製化美妝護膚報告", use_container_width=True):
    st.markdown("---")
    st.header("🎉 您的客製化美妝與護膚指南")
    
    # 🧪 膚質診斷顯示
    skin_info = SKIN_DATABASE[user_skin]
    st.info(skin_info["diagnosis"])
    
    skin_dict = skin_info[user_budget]

    # --------------------------------------------------------------------------
    # 🌙 深度夜間保養產出畫面
    # --------------------------------------------------------------------------
    if user_routine == "1":
        st.subheader("🌙 精準步驟：深度夜間保養指南")
        
        skincare_steps = [
            ("STEP 1【深層卸妝】", "makeup_remover"),
            ("STEP 2【溫和潔顏】", "cleanser"),
            ("STEP 3【密集精華】", "essence"),
            ("STEP 4【鎖水修護】", "cream")
        ]
        
        for step_title, db_key in skincare_steps:
            with st.expander(step_title, expanded=True):
                for item in skin_dict[db_key]:
                    st.markdown(f"**{item['name']}**")
                    st.caption(f"💡 推薦理由：{item['reason']}")
        
        st.subheader("📺 推薦護膚學理線上教程")
        for link_item in TUTORIAL_DATABASE["skincare"]:
            st.link_button(f"🔗 {link_item['title']}", link_item['url'])

    # --------------------------------------------------------------------------
    # 💄 四大妝容風格產出畫面
    # --------------------------------------------------------------------------
    else:
        db_key = str(int(user_routine) - 1)
        style_info = MAKEUP_STYLE_DATABASE[db_key]
        raw_makeup_lists = style_info["budget_data"][user_budget]
        
        st.subheader(f"✨ 專屬妝容風格：{style_info['style_name']}")
        
        # 1. 膚質客製化底妝
        st.markdown("#### 🪵 適合您膚質的底妝/防護推薦")
        base_steps = [
            ("STEP 1【基礎底妝/妝前】", "makeup_base"),
            ("STEP 2【局部遮瑕/粉底】", "foundation"),
            ("STEP 3【定妝控油/鎖水】", "setting_powder")
        ]
        for step_title, db_key_name in base_steps:
            with st.expander(step_title, expanded=True):
                for item in skin_dict[db_key_name]:
                    st.markdown(f"**{item['name']}**")
                    st.caption(f"💡 專屬膚質理由：{item['reason']}")
        
        # 2. 風格彩妝
        st.markdown("#### 🎨 專屬風格彩妝推薦清單")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**👁️ 推薦眼影**")
            for item in raw_makeup_lists["eyeshadow"]: st.write(item)
        with col2:
            st.markdown("**🌸 推薦腮紅**")
            for item in raw_makeup_lists["blusher"]: st.write(item)
        with col3:
            st.markdown("**💋 推薦口紅**")
            for item in raw_makeup_lists["lipstick"]: st.write(item)
            
        # 3. 影音教程
        st.markdown(" ")
        st.subheader("📺 本次妝容風格線上教程")
        style_tutorial = TUTORIAL_DATABASE["makeup_styles"][db_key]
        st.link_button(f"🎬 {style_tutorial['title']}", style_tutorial['url'])