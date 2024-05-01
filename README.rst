==========
rst-budoux
==========

Text splitter in reStructuredText by BudouX.

.. raw:: html

   <div align="center">
     <img src="https://github.com/attakei-lab/rst-budoux/blob/env/upgrade-readme/mv.png" >
   </div>

Example
=======

.. code:: rst

   Example from BudouX
   ===================

   あなたに寄り添う最先端のテクノロジー。

.. code:: console

   $ run rst2pseudoxml examples/budoux-sample-text.rst
   <document ids="example-from-budoux" names="example\ from\ budoux" source="examples/budoux-sample-text.rst" title="Example from BudouX">
       <title>
           Example from BudouX
       <paragraph>
           あなたに寄り添う最先端のテクノロジー。

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
