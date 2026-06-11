# Setup: React + Node.js + Socket.IO


このページは、**ミニ課題を始める前**に行うセットアップ用ページである。

このページでは、以下の準備を行う。

* Node.js、npm、npx が使えるか確認する
* プロジェクト用フォルダを作成する
* `server` フォルダを作成する
* React の `client` を作成する
* 必要なライブラリをインストールする
* Server と React Client の起動方法を確認する

このページが完了したら、次のページに進む。

[Week 10: Introduction to Socket.IO](week10.md)

---

<a id="1"></a>

## 1. 作成するもの

この演習では、次のようなプロジェクトを作成する。

```text
chatapp/
├── server/   ← Node.js + Socket.IO server
└── client/   ← React application
```

このプロジェクトには、2つのプログラムがある。

| Part     | Meaning               | Main file           |
| -------- | --------------------- | ------------------- |
| `server` | Node.js で動くサーバー側プログラム | `server/server.js`  |
| `client` | React で作るブラウザ側プログラム   | `client/src/App.js` |

重要な点は次の通りである。

* `server` フォルダは **自分で作成する**。
* `server.js` ファイルも **自分で作成する**。
* `client` フォルダは **React のコマンドで自動作成される**。
* `client/src/App.js` は React によって自動作成される。あとで中身を書き換える。


---

<a id="2"></a>

## 2. 先に確認するもの

React や Socket.IO を使う前に、まず以下が使えるか確認する必要がある。

| Tool    | 何に使うか                           |
| ------- | ------------------------------- |
| Node.js | JavaScript をパソコン上で実行するために使う     |
| npm     | JavaScript のライブラリをインストールするために使う |
| npx     | React プロジェクト作成などのコマンドを実行するために使う |
| VS Code | コードを書くために使う                     |

重要である。
`npx create-react-app client` を実行する前に、必ず Node.js、npm、npx を確認すること。


---

<a id="3"></a>

## 3. Node.js、npm、npx を確認する
!!! details "▼ 詳しい内容を表示"

    ### 3.1 どこで行うか

    この作業は、**VS Code Terminal** で行う。

    Windows の場合は PowerShell、macOS の場合は Terminal が開くことが多い。
    どちらでも、ここで使う基本コマンドはほとんど同じである。

    ---

    ### 3.2 Node.js の確認

    VS Code Terminal に次のコマンドを入力する。

    ```bash
    node -v
    ```

    バージョン番号が表示されれば、Node.js はインストールされている。

    例：

    ```text
    v20.11.0
    ```

    または

    ```text
    v22.11.0
    ```

    数字は人によって違ってよい。
    バージョン番号が表示されることが重要である。

    ---

    ### 3.3 npm の確認

    次に、以下のコマンドを入力する。

    ```bash
    npm -v
    ```

    バージョン番号が表示されれば、npm も使える。

    例：

    ```text
    10.2.4
    ```

    ---

    ### 3.4 npx の確認

    次に、以下のコマンドを入力する。

    ```bash
    npx -v
    ```

    バージョン番号が表示されれば、npx も使える。

    例：

    ```text
    10.2.4
    ```

    ---

    ### 3.5 確認結果

    以下の3つすべてでバージョン番号が表示されれば、次に進んでよい。

    ```bash
    node -v
    npm -v
    npx -v
    ```

    例：

    ```text
    v20.11.0
    10.2.4
    10.2.4
    ```

    もし `node`、`npm`、`npx` のどれかが認識されない場合は、次の「Node.js が入っていない場合」を読むこと。


    ---

    <a id="4"></a>

## 4. Node.js が入っていない場合
!!! details "▼ 詳しい内容を表示"

    ### 4.1 Windows の場合

    Node.js が入っていない場合は、Node.js の公式ページから **LTS** 版をインストールする。

    !!! details "Windows で Node.js をインストールする手順"

        1. Webブラウザで `Node.js download` と検索する。
        2. Node.js の公式ページを開く。
        3. **LTS** と書かれているバージョンを選ぶ。
        4. Windows Installer をダウンロードする。
        5. ダウンロードしたインストーラーを開く。
        6. 基本的には、そのまま **Next** を押してインストールする。
        7. インストールが終わったら、VS Code を一度閉じる。
        8. VS Code をもう一度開く。
        9. Terminal を開き、もう一度確認する。

        確認コマンド：

        ```bash
        node -v
        npm -v
        npx -v
        ```

        3つともバージョン番号が表示されれば、準備完了です。

    ---

    ### 4.2 macOS の場合

    Node.js が入っていない場合は、Node.js の公式ページから **LTS** 版をインストールする。

    !!! details "macOS で Node.js をインストールする手順"

        1. Webブラウザで `Node.js download` と検索する。
        2. Node.js の公式ページを開く。
        3. **LTS** と書かれているバージョンを選ぶ。
        4. macOS Installer をダウンロードする。
        5. ダウンロードしたインストーラーを開く。
        6. 基本的には、そのまま進めてインストールする。
        7. インストールが終わったら、VS Code を一度閉じる。
        8. VS Code をもう一度開く。
        9. Terminal を開き、もう一度確認する。

        確認コマンド：

        ```bash
        node -v
        npm -v
        npx -v
        ```

        3つともバージョン番号が表示されれば、準備完了です。

    ---

    ### 4.3 注意

    !!! hint "インストール後の注意"

        Node.js をインストールした直後に、古い Terminal では `node` が認識されないことがあります。
        その場合は、VS Code を閉じて、もう一度開くと改善します。


    ---

    <a id="5"></a>

## 5. VS Code を開く
!!! details "▼ 詳しい内容を表示"

    ### 5.1 VS Code で作業用フォルダを開く

    まず、Visual Studio Code を開く。

    次に、上のメニューから以下を選ぶ。

    ```text
    File → Open Folder...
    ```

    作業したい場所を選ぶ。

    例：

    ```text
    Documents
    ```

    または

    ```text
    Desktop
    ```

    ここでは、例として `Documents` や `Desktop` を使っている。
    自分が分かりやすい場所であれば、どこでもよい。


    ---

    <a id="6"></a>

## 6. VS Code Terminal を開く
!!! details "▼ 詳しい内容を表示"

    VS Code の上のメニューから以下を選ぶ。

    ```text
    Terminal → New Terminal
    ```

    画面の下に Terminal が表示される。

    Windows の場合、多くの場合は **PowerShell** が開く。
    macOS の場合、多くの場合は **zsh** または **bash** が開く。

    この資料の基本コマンドは、Windows と macOS の両方で使える。


    ---

    <a id="7"></a>

## 7. よく使うコマンド
!!! details "▼ 詳しい内容を表示"

    ここでは、このセットアップで使う基本コマンドを説明する。

    ---

    ### 7.1 `mkdir`

    `mkdir` は **make directory** の意味である。
    つまり、新しいフォルダを作るコマンドである。

    例：

    ```bash
    mkdir chatapp
    ```

    これは、`chatapp` という名前のフォルダを作成する。

    ---

    ### 7.2 `cd`

    `cd` は **change directory** の意味である。
    つまり、別のフォルダに移動するコマンドである。

    例：

    ```bash
    cd chatapp
    ```

    これは、`chatapp` フォルダの中に移動する、という意味である。

    ---

    ### 7.3 `cd ..`

    `cd ..` は、1つ上のフォルダに戻るという意味である。

    例として、現在いる場所が次の場所であるとする。

    ```text
    chatapp/server/
    ```

    ここで次のコマンドを入力する。

    ```bash
    cd ..
    ```

    すると、次の場所に戻る。

    ```text
    chatapp/
    ```

    ---

    ### 7.4 `npm`

    `npm` は JavaScript のライブラリをインストールするために使う。

    例：

    ```bash
    npm install express socket.io
    ```

    これは、`express` と `socket.io` というライブラリをインストールする。

    ---

    ### 7.5 `npx`

    `npx` は、ツールを一時的に実行するために使う。

    例：

    ```bash
    npx create-react-app client
    ```

    これは、React プロジェクトを作成するコマンドである。
    このコマンドを実行すると、`client` フォルダが自動的に作成される。


    ---

    <a id="8"></a>

## 8. プロジェクトフォルダを作成する
!!! details "▼ 詳しい内容を表示"

    ### 8.1 どこで行うか

    この作業は、**VS Code Terminal** で行う。

    今いる場所は、VS Code で開いた作業用フォルダである。

    例：

    ```text
    Documents
    ```

    または

    ```text
    Desktop
    ```

    ---

    ### 8.2 `chatapp` フォルダを作る

    VS Code Terminal に次のコマンドを入力する。

    ```bash
    mkdir chatapp
    ```

    これで、`chatapp` フォルダが作成される。

    ---

    ### 8.3 `chatapp` フォルダに移動する

    次に、以下のコマンドを入力する。

    ```bash
    cd chatapp
    ```

    これで、現在の場所は次のようになる。

    ```text
    chatapp/
    ```


    ---

    <a id="9"></a>

## 9. server フォルダを作成する
!!! details "▼ 詳しい内容を表示"

    ### 9.1 どこで行うか

    この作業は、**VS Code Terminal** で行う。

    現在いる場所が次の場所であることを確認する。

    ```text
    chatapp/
    ```

    ---

    ### 9.2 `server` フォルダを作る

    次のコマンドを入力する。

    ```bash
    mkdir server
    ```

    これで、`server` フォルダが作成される。

    現在のフォルダ構成は次のようになる。

    ```text
    chatapp/
    └── server/
    ```

    ---

    ### 9.3 `server` フォルダに移動する

    次のコマンドを入力する。

    ```bash
    cd server
    ```

    これで、現在の場所は次のようになる。

    ```text
    chatapp/server/
    ```


    ---

    <a id="10"></a>

## 10. Node.js サーバープロジェクトを初期化する
!!! details "▼ 詳しい内容を表示"

    ### 10.1 どこで行うか

    この作業は、**VS Code Terminal** で行う。

    必ず、現在いる場所が次の場所であることを確認する。

    ```text
    chatapp/server/
    ```

    ---

    ### 10.2 `npm init` を実行する

    次のコマンドを入力する。

    ```bash
    npm init -y
    ```

    このコマンドを実行すると、次のファイルが自動で作成される。

    ```text
    package.json
    ```

    ---

    ### 10.3 `package.json` とは

    `package.json` は、この Node.js プロジェクトの情報を保存するファイルである。

    たとえば、次のような情報が入る。

    * プロジェクト名
    * 使用しているライブラリ
    * 実行に必要な情報

    `package.json` は自動で作成される。
    この演習では、基本的に自分で編集する必要はない。


    ---

    <a id="11"></a>

## 11. サーバー用ライブラリをインストールする
!!! details "▼ 詳しい内容を表示"

    ### 11.1 どこで行うか

    この作業は、**VS Code Terminal** で行う。

    必ず、現在いる場所が次の場所であることを確認する。

    ```text
    chatapp/server/
    ```

    ---

    ### 11.2 `express` と `socket.io` をインストールする

    次のコマンドを入力する。

    ```bash
    npm install express socket.io
    ```

    ---

    ### 11.3 インストールされるライブラリ

    | Library     | Purpose          |
    | ----------- | ---------------- |
    | `express`   | Web サーバーを作るために使う |
    | `socket.io` | リアルタイム通信を行うために使う |

    ---

    ### 11.4 自動で作成されるもの

    このコマンドを実行すると、次のファイルやフォルダが自動で作成される。

    ```text
    server/
    ├── node_modules/
    ├── package.json
    └── package-lock.json
    ```

    ---

    ### 11.5 `node_modules` について

    `node_modules` には、インストールされたライブラリのファイルが入っている。

    `node_modules` の中身は編集しない。
    とても多くのファイルがあるが、これは正常である。


    ---

    <a id="12"></a>

## 12. server.js を作成する
!!! details "▼ 詳しい内容を表示"

    ### 12.1 どこで行うか

    この作業は、**VS Code の Explorer** で行う。

    左側のファイル一覧を使ってファイルを作成する。

    ---

    ### 12.2 `server.js` ファイルを作る

    VS Code の左側にある Explorer を見る。

    次の手順でファイルを作成する。

    1. `server` フォルダを右クリックする。
    2. **New File** を選ぶ。
    3. ファイル名として、次を入力する。

    ```text
    server.js
    ```

    ---

    ### 12.3 現在の server フォルダ

    作成後、`server` フォルダは次のようになる。

    ```text
    server/
    ├── server.js
    ├── package.json
    ├── package-lock.json
    └── node_modules/
    ```

    この時点では、`server.js` は空でよい。
    Week 10 のページでコードを書く。


    ---

    <a id="13"></a>

## 13. React Client を作成する
!!! details "▼ 詳しい内容を表示"

    ### 13.1 どこで行うか

    この作業は、**VS Code Terminal** で行う。

    まず、現在いる場所を確認する。

    もし現在の場所が次の場所なら、

    ```text
    chatapp/server/
    ```

    1つ上に戻る必要がある。

    ---

    ### 13.2 `chatapp` フォルダに戻る

    次のコマンドを入力する。

    ```bash
    cd ..
    ```

    これで、現在の場所は次のようになる。

    ```text
    chatapp/
    ```

    ---

    ### 13.3 React プロジェクトを作成する

    現在の場所が `chatapp/` であることを確認してから、次のコマンドを入力する。

    ```bash
    npx create-react-app client
    ```

    このコマンドにより、`client` フォルダが自動で作成される。

    重要である。
    `client` フォルダは自分で作らない。
    `client` フォルダは、`npx create-react-app client` によって自動で作成される。

    先に自分で `client` フォルダを作ると、エラーになる場合がある。

    ---

    ### 13.4 質問が表示された場合

    初めてこのコマンドを実行すると、Terminal に次のような質問が表示される場合がある。

    ```text
    Need to install the following packages:
    create-react-app
    Ok to proceed? (y)
    ```

    この場合は、次のように入力して Enter を押す。

    ```text
    y
    ```

    ---

    ### 13.5 時間がかかる場合

    このコマンドは数分かかることがある。

    Terminal に多くの文字が表示されるが、エラーでなければ問題ない。

    完了すると、プロジェクトは次のようになる。

    ```text
    chatapp/
    ├── server/
    └── client/
    ```


    ---

    <a id="14"></a>

## 14. Socket.IO Client をインストールする
!!! details "▼ 詳しい内容を表示"

    ### 14.1 どこで行うか

    この作業は、**VS Code Terminal** で行う。

    今は `chatapp/` にいるはずである。

    ---

    ### 14.2 `client` フォルダに移動する

    次のコマンドを入力する。

    ```bash
    cd client
    ```

    これで、現在の場所は次のようになる。

    ```text
    chatapp/client/
    ```

    ---

    ### 14.3 `socket.io-client` をインストールする

    次のコマンドを入力する。

    ```bash
    npm install socket.io-client
    ```

    このライブラリは、React から Socket.IO サーバーに接続するために使う。


    ---

    <a id="15"></a>

## 15. 最終的なフォルダ構成
!!! details "▼ 詳しい内容を表示"

    ここまで完了すると、プロジェクトは次のようになる。

    ```text
    chatapp/
    ├── server/
    │   ├── server.js
    │   ├── package.json
    │   ├── package-lock.json
    │   └── node_modules/
    │
    └── client/
        ├── src/
        │   └── App.js
        ├── package.json
        ├── package-lock.json
        └── node_modules/
    ```

    Week 10 で主に編集するファイルは次の2つである。

    ```text
    chatapp/server/server.js
    chatapp/client/src/App.js
    ```


    ---

    <a id="16"></a>

## 16. Server の起動方法
!!! details "▼ 詳しい内容を表示"

    サーバーと React は別々のプログラムである。
    そのため、**VS Code Terminal を2つ**使う。

    ### 16.1 どこで行うか

    この作業は、**1つ目の VS Code Terminal** で行う。

    この Terminal は Server 用である。

    ---

    ### 16.2 `server` フォルダに移動する

    `server` フォルダに移動する。

    もし VS Code Terminal が最初の作業フォルダにいる場合は、次のように入力する。

    ```bash
    cd chatapp/server
    ```

    もしすでに `chatapp/` にいる場合は、次のように入力する。

    ```bash
    cd server
    ```

    もしすでに `chatapp/server/` にいる場合は、移動する必要はない。

    ---

    ### 16.3 Server を起動する

    `chatapp/server/` にいる状態で、次を実行する。

    ```bash
    node server.js
    ```

    `server.js` に正しいコードが書かれていれば、次のような表示が出る。

    ```text
    Server running at http://localhost:3001
    ```

    Week 10 のコードを書く前は、`server.js` が空のため、まだ正しく起動しない場合がある。
    Week 10 で `server.js` のコードを書いたあとに、このコマンドを実行する。


    ---

    <a id="17"></a>

## 17. React Client の起動方法
!!! details "▼ 詳しい内容を表示"

    ### 17.1 どこで行うか

    この作業は、**2つ目の VS Code Terminal** で行う。

    新しい Terminal を開く。

    ```text
    Terminal → New Terminal
    ```

    この Terminal は React Client 用である。

    ---

    ### 17.2 `client` フォルダに移動する

    `client` フォルダに移動する。

    もし VS Code Terminal が最初の作業フォルダにいる場合は、次のように入力する。

    ```bash
    cd chatapp/client
    ```

    もしすでに `chatapp/` にいる場合は、次のように入力する。

    ```bash
    cd client
    ```

    もしすでに `chatapp/client/` にいる場合は、移動する必要はない。

    ---

    ### 17.3 React を起動する

    `chatapp/client/` にいる状態で、次を実行する。

    ```bash
    npm start
    ```

    ブラウザが自動で開く。

    React は通常、次の URL で開く。

    ```text
    http://localhost:3000
    ```


    ---

    <a id="18"></a>

## 18. 変更したときの注意
!!! details "▼ 詳しい内容を表示"

    ### 18.1 `App.js` を変更した場合

    `App.js` は React 側のファイルである。

    場所：

    ```text
    chatapp/client/src/App.js
    ```

    `App.js` を変更した場合は、基本的に次の操作だけでよい。

    ```text
    保存する
    ```

    React は自動的にブラウザを更新する。
    そのため、通常は `npm start` をやり直す必要はない。

    ---

    ### 18.2 `server.js` を変更した場合

    `server.js` はサーバー側のファイルである。

    場所：

    ```text
    chatapp/server/server.js
    ```

    `server.js` を変更した場合は、サーバーを再起動する必要がある。

    手順：

    1. `server.js` を保存する。
    2. Server を動かしている Terminal をクリックする。
    3. 次のキーを押して Server を止める。

    ```text
    Ctrl + C
    ```

    4. もう一度 Server を起動する。

    ```bash
    node server.js
    ```

    重要である。
    `server.js` を変更しても、Server を再起動しなければ新しいコードは反映されない。


    ---

    <a id="19"></a>

## 19. よくあるエラー
!!! details "▼ 詳しい内容を表示"

    ### 19.1 `node` が認識されない

    次のようなエラーが出る場合がある。

    ```text
    node is not recognized
    ```

    または

    ```text
    command not found: node
    ```

    この場合、Node.js が入っていない、または Terminal が古い状態である可能性がある。

    対処方法：

    1. Node.js の LTS 版をインストールする。
    2. VS Code を一度閉じる。
    3. VS Code をもう一度開く。
    4. Terminal を開き直す。
    5. 次を確認する。

    ```bash
    node -v
    npm -v
    npx -v
    ```

    ---

    ### 19.2 `npm` が認識されない

    Node.js をインストールすると、通常 npm も一緒に使えるようになる。

    対処方法：

    1. Node.js の LTS 版をインストールし直す。
    2. VS Code を一度閉じる。
    3. VS Code をもう一度開く。
    4. Terminal を開き直す。
    5. 次を確認する。

    ```bash
    npm -v
    ```

    ---

    ### 19.3 `npx` が認識されない

    `npx` が認識されない場合は、Node.js または npm が正しく入っていない可能性がある。

    対処方法：

    1. Node.js の LTS 版をインストールし直す。
    2. VS Code を一度閉じる。
    3. VS Code をもう一度開く。
    4. Terminal を開き直す。
    5. 次を確認する。

    ```bash
    npx -v
    ```

    ---

    ### 19.4 `client` フォルダ作成でエラーになる

    `npx create-react-app client` でエラーになる場合、すでに `client` フォルダを作ってしまっている可能性がある。

    確認すること：

    ```text
    chatapp/client/
    ```

    がすでに存在していないか確認する。

    もし空の `client` フォルダを自分で作ってしまった場合は、そのフォルダを削除してから、もう一度以下を実行する。

    ```bash
    npx create-react-app client
    ```

    ---

    ### 19.5 Server と React を同じ Terminal で起動しようとしている

    Server と React は別々のプログラムである。
    そのため、Terminal を2つ使う必要がある。

    | Terminal   | 場所                | 実行するコマンド         |
    | ---------- | ----------------- | ---------------- |
    | Terminal 1 | `chatapp/server/` | `node server.js` |
    | Terminal 2 | `chatapp/client/` | `npm start`      |

    ---

    ### 19.6 `server.js` を変更したのに反映されない

    `server.js` を変更した場合は、Server を再起動する必要がある。

    手順：

    ```text
    Ctrl + C
    ```

    そのあと、もう一度実行する。

    ```bash
    node server.js
    ```


    ---

    <a id="20"></a>

## 20. セットアップ確認チェックリスト
!!! details "▼ 詳しい内容を表示"

    Week 10 を始める前に、次の項目を確認する。

    * [ ] `node -v` でバージョン番号が表示された。
    * [ ] `npm -v` でバージョン番号が表示された。
    * [ ] `npx -v` でバージョン番号が表示された。
    * [ ] `chatapp` フォルダを作成した。
    * [ ] `chatapp/server` フォルダを作成した。
    * [ ] `server.js` ファイルを作成した。
    * [ ] `server` フォルダ内で `npm init -y` を実行した。
    * [ ] `server` フォルダ内で `express` と `socket.io` をインストールした。
    * [ ] `npx create-react-app client` を使って React アプリを作成した。
    * [ ] `client` フォルダ内で `socket.io-client` をインストールした。
    * [ ] `client/src/App.js` が存在することを確認した。
    * [ ] Server の起動には `chatapp/server` で `node server.js` を使うことを確認した。
    * [ ] React Client の起動には `chatapp/client` で `npm start` を使うことを確認した。
    * [ ] Server と React Client は別々の Terminal で起動することを確認した。

    すべて完了したら、次のページに進む。

    [Week 10: Introduction to Socket.IO](week10.md)

