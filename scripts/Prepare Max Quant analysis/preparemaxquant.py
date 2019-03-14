import xml.etree.ElementTree as ET



def clear_parameter_tree(xml_tree):
    """Returns an xml tree object from MaxQuant's mqpar.xml that has some parts missing."""
    root = xml_tree.getroot()
    for name in ['filePaths', 'experiments', 'fractions', 'ptms', 'paramGroupIndices', 'commonChannel']:
        Child = next(root.iter(name))
        for _ in range(2):
            for short in Child:
                Child.remove(short)


def fill_parameter_tree(tree, filename):
    """Modifies an xml tree object from MaxQuant's mqpar.xml file to include a raw filename to process."""
    data = [
        ('filePaths', 'string', filename),
        ('experiments', 'short', filename),
        ('fractions', 'short', '32767'),
        ('ptms', 'boolean', 'False'),
        ('paramGroupIndices', 'int', '0'),
        ('commonChannel', 'string', '')
    ]

    for child, tag, text in data:
        element = ET.Element(tag)
        element.text = text
        next(tree.iter(child)).append(element)

def main(rawfilename, template_filename, num_threads, parameterfilename):

    tree = ET.parse(template_filename)
    clear_parameter_tree(tree)

    fill_parameter_tree(tree, filename=rawfilename)

    numThreads = next(tree.iter('numThreads'))
    numThreads.text = str(num_threads)
    # ET.dump(numThreads)

    tree.write(analysis_directory + "mqpar.xml")


if __name__ == '__main__':






import argparse
parser = argparse.ArgumentParser(description="Prepare MaxQuant Analysis.")
parser.add_argument('Fasta_complete', help="The Fasta File used for the analysis")
parser.add_argument('Rawfilepath_complete', help="Raw-File Path in analysis directory")
parser.add_argument('template_path_complete', help="MQ parameter file complete path")
parser.add_argument('Analysis_directory', help="The Folder where the MQ analysis will take place")
parser.add_argument('Threads', help="Number of threads used for analysis (default=2)")
parser.add_argument('template_output', help="MQ parameter file used for the analysis")

args = parser.parse_args()

main(Fasta=args.Fasta_complete, rawfilepath=args.Rawfilepath_complete, template=args.template_path_complete, analysis_directory=args.Analysis_directory, Threads=args.Threads, output_template=args.template_output' )

