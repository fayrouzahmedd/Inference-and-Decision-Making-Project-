def parse_paragraph(paragraph):
    sentences = paragraph.split('. ')
    premises = sentences[:-1]
    conclusion = sentences[-1]
    return sentences, premises, conclusion

paragraph = input("Enter a paragraph in the form 'Premise 1. Premise 2. ... Conclusion.': ")
sentences, premises, conclusion = parse_paragraph(paragraph)
print("sentences are", sentences)
print("premises are", premises)
print("conclusion is", conclusion)