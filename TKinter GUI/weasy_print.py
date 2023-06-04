from pathlib import Path
import sys

from weasyprint import HTML


def makepdf(html):
    """Generate a PDF file from a string of HTML."""
    print("FIFTH")
    # htmldoc = HTML(string=html, base_url="")
    try:
        print("SIXTH")
        htmldoc = HTML(string=html, base_url="").write_pdf(target="sample.pdf")
    except Exception as e:
        print(e)
    return htmldoc


def run():
    """Command runner."""
    print("FIRST")
    # print(Path(outfile))
    # infile = "sys.argv[1]"
    infile = "index.html"
    print("SECOND")
    outfile = "sample.pdf"
    print("THIRD")
    # outfile = sys.argv[2]
    html = Path(infile).read_text()
    print("FORTH")
    pdf = makepdf(html)
    print("SEVENTH")
    Path(outfile).write_bytes(pdf)
    print("EIGHTTH")


# if __name__ == "__main__":
print("HELLO")
run()