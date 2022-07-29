import csv
from pyhamilton import (LayoutManager, Plate96, ResourceType, resource_list_with_prefix)


lmgr = LayoutManager('CherryPicking96to384.lay')

target_plate = lmgr.assign_unused_resource(ResourceType(Plate96, 'TargetPlate1'))
source_plates = resource_list_with_prefix(lmgr, 'SourcePlate', Plate96, 6)

plate_str_to_obj = {k.layout_name():k for k in source_plates}
plate_str_to_obj.update({'TargetPlate1': target_plate})


def well_to_index_96(well: str):
    #split_str = list(well)
    letter = (ord(well[0]) - 65)
    number = (int(well[1:])-1)*8
    return letter + number

def worklist_96(file_path):

    target_dict = {}

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            target_plate = row[3]
            target_well = well_to_index_96(row[4])
            target_tuple = (plate_str_to_obj[target_plate], target_well)
            if target_tuple not in target_dict:
                target_dict.update({target_tuple:[]})

            source_plate = row[1]
            source_well = well_to_index_96(row[2])
            source_tuple = (plate_str_to_obj[source_plate], source_well)
            target_dict[target_tuple].append(source_tuple)

        return target_dict

if __name__=='__main__':
    a = worklist_96('061322_32Seqs.csv')
    #IPython.embed()
