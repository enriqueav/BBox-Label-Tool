# -*- coding: utf-8 -*-

from lxml import etree

def createXML(jpg_file, boxes, img_size):
    annotation = etree.Element('annotation')

    fo = etree.Element('folder')
    fo.text = 'images'
    annotation.append(fo)

    f = etree.Element('filename')
    f.text = jpg_file.decode('UTF-8')
    annotation.append(f)

    size = etree.Element('size')
    w = etree.Element('width')
    w.text = str(img_size[0])
    h = etree.Element('height')
    h.text = str(img_size[1])
    d = etree.Element('depth')
    d.text = str(3)

    size.append(w)
    size.append(h)
    size.append(d)
    annotation.append(size)

    seg = etree.Element('segmented')
    seg.text = str(0)
    annotation.append(seg)

    for box in boxes:
        object = etree.Element('object')
        n = etree.Element('name')
        p = etree.Element('pose')
        t = etree.Element('truncated')
        d_1 = etree.Element('difficult')
        bb = etree.Element('bndbox')

        # TODO: change this to proper class name
        n.text = 'class'
        p.text = 'center'
        t.text = str(1)
        d_1.text = str(0)

        xmi = etree.Element('xmin')
        ymi = etree.Element('ymin')
        xma = etree.Element('xmax')
        yma = etree.Element('ymax')

        xmi.text = str(box[0])
        ymi.text = str(box[1])
        xma.text = str(box[2])
        yma.text = str(box[3])

        bb.append(xmi)
        bb.append(ymi)
        bb.append(xma)
        bb.append(yma)

        object.append(n)
        object.append(p)
        object.append(t)
        object.append(d_1)
        object.append(bb)

        annotation.append(object)

    return annotation


def saveXML(xml, filename_xml):
    with open(filename_xml, "w") as file:
        file.write(etree.tostring(xml, pretty_print=True))


def createXMLAnnotation(jpg_file, boxes, img_size, filename_xml):
    xml = createXML(jpg_file, boxes, img_size)
    saveXML(xml, filename_xml)
