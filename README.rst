==========
rst-budoux
==========

.. list-table::

   * - Badges
     - .. image:: https://img.shields.io/pypi/v/rst-budoux.svg
          :target: https://pypi.org/project/rst-budoux/
     - .. image:: https://github.com/attakei-lab/rst-budoux/actions/workflows/main.yml/badge.svg
          :target: https://github.com/attakei-lab/rst-budoux/actions
     - .. image:: https://readthedocs.org/projects/rst-budoux/badge/?version=stable
          :target: https://rst-budoux.readthedocs.io/en/sable

Text splitter in reStructuredText by BudouX.

.. image:: https://raw.githubusercontent.com/attakei-lab/rst-budoux/main/mv.png
   :align: center
   :width: 50%

.. note::

   `日本語での説明があります。 <https://github.com/attakei-lab/rst-budoux/blob/main/README_ja.rst>`_

Overview
========

This is bridge library to ``docutils`` and ``budoux``.
You can break lines naturally when build contents from reStructuredText by using this.

See `document <https://rst-budoux.readthedocs.io/>`_ for more information.

Usage
=====

You can install from PyPI.

.. code:: console

   pip install rst-budoux

This provides also as Sphinx-extension, therefore it works to register into your ``conf.py``.

.. code:: python

   extensions = [
       "rst_budoux.sphinx",
   ]

You want to use wihout Sphinx ? Please see `document <https://rst-budoux.readthedocs.io/>`_.

Example
=======

This is example using psuedoxml outputs for "docutils only" and "with rst-budoux".

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
