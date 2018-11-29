from voc_eval import voc_eval

print(voc_eval('/home/rgj/darknet/results/{}.txt', '/home/rgj/darknet/scripts/Data_v1/Annotations/{}.xml', '/home/rgj/darknet/scripts/Data_v1/ImageSets/Main/test.txt', 'car', '.'))
