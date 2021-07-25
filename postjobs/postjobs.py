def print_output(taskbook):

    output = taskbook['output']

    #pprint(output)
    # Print task results
    print(f"Task = {output['task']}")

    for result in sorted(output['devices'], key=lambda k: k['device']):
        print('='*20,f"Results for {result['device']}",'='*20)
        if 'exception' not in result:
            # if no exception in main loop we should have a dictionary or a list of dictionaries
            # each containing a 'result'
            if isinstance(result['result'], list):
                for r in result['result']:
                    print('-'*len(r['task']))
                    print(r['task'])
                    print('-'*len(r['task']))
                    pprint(r['result'])
                    print()
            elif isinstance(result['result'], dict):
                print(result['result']['result']) # definitely needs improvement!
            else:
                print(result['result'])    
        else:
            print(result['result'])
    print()


def print_elapsed(taskbook):
    print('-'*35)
    print("Elapsed time: {}".format(taskbook['elapsed_time']))
    print('-'*35)
