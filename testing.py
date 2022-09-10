import csv
import shutil
f = open('aoi_label.csv')
csv_f = csv.reader(f)
data = []
for row in csv_f:
   data.append(row)
f.close()

def convert_row(row):
    try:
        name = row[1]
        source = f"aoi/defect/{name}"
        destination = f"aoi/labeling/{name}"
        shutil.copyfile(source, destination)
        f = open(f"aoi/labeling/{name[:-4]}.xml", "w")
        data = """
        <annotation>
        <folder>practice</folder>
        <idx>%s</idx>
        <path>%s</path>
        <object>
            <name>%s</name>
            <bndbox>
                <xmin>%s</xmin>
                <ymin>%s</ymin>
                <xmax>%s</xmax>
                <ymax>%s</ymax>
            </bndbox>
        </object>
    </annotation> """ %(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    
        f.write(data)
        f.close()
    except:
        pass
([convert_row(row) for row in data[:500]])