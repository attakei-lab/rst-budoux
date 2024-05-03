==========
rst-budoux
==========

reStructuredTextのテキストを分かち書きするライブラリです。

.. image:: https://github.com/attakei-lab/rst-budoux/blob/main/mv.png
   :align: center

概要
====

reStructuredTextをパースしたdoctreeに手を加えて、日本語文を分かち書きされた状態に変換します。

具体的には
----------

このようなreStructuredTextのソースを用意します。

.. code:: rst

   Example from BudouX
   ===================

   あなたに寄り添う最先端のテクノロジー。


docutilsの ``rst2pseudoxml`` を使うと、内部ではこのような構成としてパースしていることが分かります。

.. code:: console

   $ run rst2pseudoxml examples/budoux-sample-text.rst
   <document ids="example-from-budoux" names="example\ from\ budoux" source="examples/budoux-sample-text.rst" title="Example from BudouX">
       <title>
           Example from BudouX
       <paragraph>
           あなたに寄り添う最先端のテクノロジー。

``rst-budoux`` を用いた ``rst-budoux2pseudoxml`` を使うと、分かち書きを行った下記のような構成に編集します。

.. code:: console

   $ run rst-budoux2pseudoxml examples/budoux-sample-text.rst
   <document ids="example-from-budoux" names="example\ from\ budoux" source="examples/budoux-sample-text.rst" title="Example from BudouX">
       <title>
           Example from BudouX
       <paragraph>
           あなたに
           <word-break>
           寄り添う
           <word-break>
           最先端の
           <word-break>
           テクノロジー。

機能
====

コア機能としては、
「BudouXのパーサーに従ってテキストを分かち書きされた状態に分割する」
「分割された間に【区切り可能】であることを示すノードの挿入する」
という2点のみです。

もちろん、自身を含めてこれだけだと不便ではあるため、次のものを同梱しています。

* 動作を参照可能にするCLIツール。
* Sphinx拡張。

使い方
======

インストール
------------

.. code:: console

   pip install rst-budoux

ライブラリとしての利用法
------------------------

.. code:: python

   import budoux
   from rst_budoux import parse_all_sentences

   document = func(...)

   # docutilsのdoctreeを生成するコードからdoctreeを受け取った後の実装例
   parser = budoux.load_default_japanese_parser()
   document = parse_all_sentences(parser, document)

   ...

Sphinxを経由しての利用例
------------------------

.. code:: python

   extensions = [
      ...,
      "rst_budoux.sphinx",
   ]

   budoux_html_separator = "<wbr>"
   buxoux_html_append_style = """
       body {
           word-break: keep-all;
           overflow-wrap: anywhere;
       }
   """
