==========
Sphinx拡張
==========

より一般的なユースケースへの対応として、Sphinx拡張として使用することが出来ます。

セットアップ
============

:doc:`installation` をもとにインストールを実施後、Sphinxドキュメントの ``conf.py`` にSphinx拡張の登録をしてください。

.. code-block:: python
   :name: conf.py
   :caption: conf.py

   extensions = [
       "rst_budoux.sphinx",
   ]

動作
====

このライブラリは新しいビルダーを提供しないため、普段どおりにドキュメントのビルドを行ってください。

設定
====

動作を調整するために、いくつかの設定項目があります。

.. confval:: budoux_separator
   :type: str
   :required: False
   :default: ``"\u200b"`` (ゼロ幅スペース)

   ``WordBreak`` ノード(=分かち書きの境界)に挿入する文字列を指定します。
   例えば、 ``"<wbr>"`` のような指定することで、HTMLタグの挿入も可能です。

.. confval:: budoux_additional_style
   :type: str | None
   :required: False
   :default: ``None``

   :confval:`budoux_separator` で挿入した文字列向けに、必要に応じてスタイルシートを記述するための項目です。
   ``html`` 系のビルダーの利用時のみ有効です。

   * ``None`` ではなく文字列を設定する場合、 ``<style> ~~ </style>`` の中身として使用します。
     必ず文法として正しいスタイルシート定義となるようにしてください。
   * この値は「そのドキュメントが ``WordBreak`` ノードを持つか否か」に関わらず、全てのページに対して作用します。
