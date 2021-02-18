import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--obsfiles', type=str, nargs='+', help='Observation file to read', required=True)
    parser.add_argument('--outfile', type=str,  help='Output file', required=True)
 
    args = parser.parse_args()
    
    obsfiles = args.obsfiles
    outfile = args.outfile

    print("Number obsfiles {}".format(len(obsfiles)))

    allstates = None
    allactions = None

    for obsfile in obsfiles:
    
        try: 
            with open(obsfile, 'r') as infile:
                obsjson = json.load(infile)
                statelist = obsjson["States"]
                actionlist = obsjson["Actions"]
                print("Num trajectories {}/{} in {}".format(len(statelist), len(actionlist), obsfile))

                if allstates == None:

                    allstates = statelist
                    allactions = actionlist

                else:

                    allstates.extend(statelist)
                    allactions.extend(actionlist)
        except:
            print("WARNING: Could not read file {}".format(obsfile))


    output = {}
    output["States"] = allstates
    output["Actions"] = allactions

    print("Total found trajectories {}".format(len(allstates)))

    with open(outfile, 'w') as outf:
        json.dump(output, outf)
        print("Finshed writing observations")


