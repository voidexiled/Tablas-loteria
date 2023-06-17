from fpdf import FPDF
import os

if __name__ == "__main__":
        tablas = os.listdir("tablas")
        pdf = FPDF(orientation = 'P', unit = 'cm', format = 'A4')
        pdf.add_page()
        tablascontadas = 0
        ekis = 3
        ye = 1
        xOffset = 0
        yOffset = 0
        for tabla in tablas:
                if tablascontadas == 0:
                        xOffset = 0 + ekis
                        yOffset = 0 + ye
                if tablascontadas == 1:
                        xOffset = 7.6 + ekis
                        yOffset = 0 + ye
                if tablascontadas == 2:
                        xOffset = 0 + ekis
                        yOffset = 12.4 + ye
                if tablascontadas == 3:
                        xOffset = 7.6 + ekis
                        yOffset = 12.4 + ye
                print(f"tabla: {tabla}, xOffset: {xOffset}, yOffset: {yOffset}")
                pdf.image(f'tablas/{tabla}', x = xOffset, y = yOffset, w = 7.6, h = 12.4)
                tablascontadas += 1
                if tablascontadas == 4:
                        tablascontadas = 0
                        
                        pdf.add_page()
        pdf.output("pdf-with-image.pdf") 