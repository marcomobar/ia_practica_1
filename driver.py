import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def bc_test_questions():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('diagnostico_rules') #STUDENTS: you will need to edit the name of your rule file here


    try:
        with engine.prove_goal('diagnostico_rules.diagnostico($enfermedad)') as gen:
            for vars, plan in gen:
                print("El diagnostico es: %s" % (vars['enfermedad']))
        with engine.prove_goal('diagnostico_rules.requiere($tratamiento, $enfermedad)') as gen:
            for vars, plan in gen:
                print("Requiere: %s" % (vars['tratamiento']))

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")

if __name__ == '__main__':
    bc_test_questions()
   