============
インストール
============

.. note:: PyPIに公開予定のため、その前提で説明しています。

pipを始めとした、パッケージ管理ツールでインストール出来ます。

.. code:: console

   pip install rst-budoux

.. code:: console

   rye add rst-budoux

Sphinxの使用を前提としている場合は、optional-dependenciesを指定してインストール出来ます。 [#]_

.. code:: console

   pip install 'rst-budoux[sphinx]'

.. [#] Sphinxがすでにインストールされていることが多いのですが、依存バージョンの関係でこの指定方法を推奨します。
