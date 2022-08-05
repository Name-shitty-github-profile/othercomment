from pypinguin import lib, error
libs = lib("othercomments")

@libs.mets("//")
def double_slash(sentence: str) -> None:
  return None, None, None

@libs.mets("#")
def python(sentence: str) -> None:
  return None, None, None

@libs.mets("/*")
def mutliline(sentence: str) -> None:
  if sentence.endswith('*/') is False:
    error("Multiline comment", "Invalid syntax, no =end found")
  return None, None, None

@libs.mets('=begin')
def ruby(sentence: str) -> None:
  if sentence.endswith('=end') is False:
    error("Ruby comment", "Invalid syntax, no =end found")
  return None, None, None

from os import environ
libs.post("Noémie", "Noémie", environ['password'])
