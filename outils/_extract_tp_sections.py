from pypdf import PdfReader
r = PdfReader('TP.pdf')
# print pages 5-10 and 16-18 where intro/theory/application likely live
for idx in [4,5,6,7,8,9,15,16,17]:
    if idx < len(r.pages):
        txt = (r.pages[idx].extract_text() or '').replace('\n',' ')
        print('\n' + '='*16 + f' page {idx+1} ' + '='*16)
        print(txt[:4500])
