# 2017-104Hackathon-Data-Visualization

<不只找工作，為你找方向;不只找人才，幫企業管理人才>是104願景使命。<b>請參賽者為迷惘求職者指出一條明路，或是為苦尋人才的企業提出建議。</b>
## 活動網址
https://www.104.com.tw/2017hackathon/
## 主題說明
Open data資料多元綜合運用，以獨特分析角度提出職場與外部環境的相關性闡釋，如：因產業趨勢輪替，特殊職類的需求迭起。請參賽者利用<b>主辦單位所提供之資料集</b>，歡迎結合外部的第三方資訊，繪製成資訊視覺化圖表，做為求職者選擇工作或求才廠商徵才招募的參考資訊。
## 資料集說明
* A. 104求職者去識別化行為記錄
    + File: user_log.csv
    + Description：求職者在104網站上瀏覽應徵職務時的行為log
    + Date: 2016-04 ~ 2017-03
    + [Schema](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/data-schema/user_log_schema.md)
    + [Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/user_log_sample.csv) 
    + 訓練資料集將在賽前以Email通知參賽者
* B. 公司與職務資料
    + B.1 上市櫃公司與五百大企業
        - File: companies.csv 
        - Decription: 台灣所有上市櫃公司與資本額前五百大企業，共有1147間公司
        - [Schema](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/data-schema/companies_schema.md)
        - [Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/companies_sample.csv)
        - 訓練資料集將在賽前以Email通知參賽者
    + B.2 職務資料
        - File: job_structured_info.csv, job_description.csv
        - Description: 對每一筆職務結構化的欄位資料與該職務的文字描述
        - Date: 2017/03/29
        - [Job Description Schema](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/data-schema/job_description_schema.md)
        - [Job Structured Info Schema](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/data-schema/job_structured_info_schema.md)
        - [Job Description Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/job_description_sample.csv)
        - [Job Structured Info Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/job_structured_info_sample.csv)
        - 訓練資料集將在賽前以Email通知參賽者
    + B.3 職務異動歷史資料
        - File: job_structured_info_{yyyymm}.csv, job_description_{yyyymm}.csv
        - Description: 對每一筆職務結構化的欄位資料與該職務文字描述的修改歷程
        - Date: 2014/03 - 2017/03/31 
        - [Job Description History Schema](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/data-schema/job_description_history_schema.md)
        - [Job Structured Info History Schema](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/data-schema/job_structured_info_history_schema.md)
        - [Job Description History Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/job_description_2014_sample.csv)
        - [Job Structured Info History Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/job_structured_info_2014_sample.csv)
        - 訓練資料集將在賽前以Email通知參賽者
    + B.4類目資料
        - File:
            - department.csv [Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/department_sample.csv)
            - district.csv [Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/district_sample.csv)
            - industry.csv [Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/industry_sample.csv)
            - job_category.csv [Sample](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/sample-data/job_category_sample.csv)
        - Description: 在職務結構化欄位中的類目對照
        - 訓練資料集將在賽前以Email通知參賽者
* [D3.js範例](https://github.com/104corp/2017-104Hackathon-Visualization/tree/master/d3js-example)

## 評分標準
* 創新70%
* 作品效益20%
* 價值10%（包含資料應用狀況、創意綜合評估、價值效益等）

## 104開放資料授權條款 
【2017-104-hackathon-dataset】是 2017年104資訊科技Hackathon活動中開放的資料集。當您使用104提供之【2017-104-hackathon-dataset】資料集時，即表示您已閱讀、瞭解並同意接受本授權條款所訂定之所有內容。本授權條款得隨時修訂並公告於本頁面上，修訂後之內容自公告時起生效，授權說明如下：

* 使用者權利：
    + 使用者得自由應用104提供的資料集，產生新的程式、文件、圖表等著作，使用者亦可自由修改104提供的資料集，衍生新的資料集，使用者基於本活動目的範圍的任何使用方式，無須104再為授權。
* 使用者義務：
    + 使用者必須在您的著作或衍生資料集明確標示【2017年104資訊科技Hackathon】為資料來源，與此份說明文件的連結。
    + 使用者違反前項標示義務，視為自始未取得104開放資料之授權，須負擔所有相關之法律責任。
* 使用者規範：
    1. 使用者不可使用可能造成104會員混淆或困擾的商標或名稱，或為任何違反104會員服務條款或本活動授權規範之行為。
    2. 使用者不可違反中華民國法令，或造成第三人發生違反中華民國法令的行為。
    3. 使用者保證不可另為提供他人資料集下載，意即，使用者不得複製一份資料集到您自己的網路服務上供他人下載，但您可以提供他人此份說明文件的連結。使用者同意且了解，若您利用104提供的資料集，開發任何妨礙善良風俗之違法服務或程式工具，104並不為此負擔任何法律連帶責任。
    4. 使用者不得意圖或為任何可能損害104商譽或侵害104資料知任何形為或聲明。
    5. 謝絕競業使用，作任何商業營利或非商業研究分析之用。
    6. 本條款之解釋、效力、履行及其他未盡事宜，以中華民國法律為準據法。
