import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def obtener_diagnostico():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('diagnostico_rules') #STUDENTS: you will need to edit the name of your rule file here


    try:
        with engine.prove_goal('diagnostico_rules.diagnostico($enfermedad)') as gen:
            for vars, plan in gen:
                print('\n')
                print('###########################')
                enfermedad = vars['enfermedad']
                print("El diagnostico es: %s" % (vars['enfermedad']))
                print('###########################')
                break
        tratamiento_goal_string = f'diagnostico_rules.requiere($tratamiento, {enfermedad})'
        with engine.prove_goal(tratamiento_goal_string) as gen:
            for vars, plan in gen:
                print('\n')
                print('###########################')
                print("Requiere: %s" % (vars['tratamiento']))
                print('###########################')
                break

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")

if __name__ == '__main__':
    obtener_diagnostico()
   