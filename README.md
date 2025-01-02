# crawler

- [crawler](#crawler)
  - [目錄架構](#目錄架構)
  - [環境設定](#環境設定)
  - [系統執行](#系統執行)

## 目錄架構
```
.
├── data                               - 存放data
│   ├── output                         - 輸出資料
│   ├── raw                            - 原始資料
│   └── interim                        - 處理過的資料
├── logs                               - 日誌
├── models                             - 存放模型
├── notebooks                          - 實驗性的 code、EDA等，等確認完後再包成 py 檔
├── poetry.lock                        - poetry 環境相關文檔
├── pyproject.toml                     - poetry 依賴的 package 及版本
├── README.md                          - 說明文件
├── requirements.txt                   - pip 依賴的 package 及版本
└──src                                - source code
    ├── models                         - 主要算法
    ├── config                         - 設定檔
    └── utils                          - 工具函式
```


## 環境設定

- 套件管理 
    - poetry [使用指南](https://blog.kyomind.tw/python-poetry/)
        - 安裝 pyproject.toml 裡的套件
            ```bash
            poetry install --no-root
            ```
        - 進入環境
            ```bash
            poetry shell
            ```
        - 退出環境
            ```bash
            exit
            ```
        - 新增套件
            ```bash
            poetry add [Package]
            ```
        - 移除套件
            ```bash
            poetry remove [Package]
            ```
        - 匯出 requirements.txt
            ```bash
            poetry export -f requirements.txt -o requirements.txt --without-hashes --dev
            ```
    - pip
        - 安裝 requirements.txt 裡的套件
            ```bash
            pip install -r requirements.txt
            ```


## 系統執行

- 執行
  - 訓練模型
    - 啟動 mlflow server 紀錄訓練過程
        ```bash
        mlflow server --host 0.0.0.0 --port 5000
        ```
    - 瀏覽器查看 mlflow server
        - http://localhost:5000/
    - 訓練模型
      - 目前於 `notebooks/train.ipynb` 中訓練
  
- 設置訓練實驗參數
    - 訓練參數放置於 `src/config/expriment/config.yml` 下，可根據不同實驗做設置