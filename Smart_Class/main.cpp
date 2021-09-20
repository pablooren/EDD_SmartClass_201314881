#include <iostream>
#include <stdlib.h>
#include "ListaA.h"

using namespace std;

int main()
{
    ListaA *lista = new ListaA();
    lista->IngresarA(201314881,21,"Juan Orellana","Sistemas","pablooren18@gmail.com","1234",210,26);
    lista->IngresarA(201314882,22,"Pablo Orellana","Sistemas","pablooren18@gmail.com","1234",210,26);
    lista->IngresarA(201314883,23,"Jose Orellana","Sistemas","pablooren18@gmail.com","1234",210,26);
    lista->IngresarA(201314884,24,"Mario Orellana","Sistemas","pablooren18@gmail.com","1234",210,26);
    lista->IngresarA(201314885,25,"Cesar Orellana","Sistemas","pablooren18@gmail.com","1234",210,26);
    lista->IngresarA(201314886,26,"Javier Orellana","Sistemas","pablooren18@gmail.com","1234",210,26);

    lista->MostrarL();

    lista->ModificarA(66);
    lista->MostrarL();

    return 0;

}
