#include "ListaA.h"
#include <iostream>
#include <stdlib.h>


using namespace std;

ListaA::ListaA()
{
    //ctor
        this->tam = 0;
        this->inicio = nullptr;
        this->fin = nullptr;
}
bool ListaA::ListaVacia(){
    if (this->tam ==0){
        return true;
    } else{
    return false;
    }

}

void ListaA::IngresarA(int carnet_,int dpi_,string nombre_,string carrera_,string correo_,string pass_,int creditos_,int edad_){
   //aqui vamos a validad los datos correctos de dpi, correo

    alumno *nuevo = new alumno(carnet_,dpi_,nombre_,carrera_,correo_,pass_,creditos_,edad_,nullptr,nullptr);
    if(this->ListaVacia()==true){
            this->inicio= nuevo;
            this->fin= nuevo;
            this->tam++;
            this->inicio->siguiente = this->fin;
            this->fin->anterior=this->inicio;
            cout<<"se ingreso el primer dato"<<endl;

    }else{
            nuevo->siguiente=this->inicio;
            nuevo->anterior=this->fin;
            this->fin->siguiente = nuevo;
            this->inicio->anterior=nuevo;
            this->fin=nuevo;
            this->tam++;
            cout<<"Se ingreso un dato"<<endl;

    }

}// end de ingresar
void ListaA::MostrarL(){
    alumno *aux = this->inicio;
    int au=0;
    while (au !=this->tam){
        cout<<"carnet: "<<aux->carnet<<" nombre: "<<aux->nombre<<" dpi: "<<aux->dpi<<endl;
        aux=aux->siguiente;
        au++;

    }

}// end de mostrar

int ListaA::ModificarA(int dpi_){
    alumno *aux = this->inicio;
    int au=0;
    while (au !=this->tam){
        if(aux->dpi==dpi_){
            cout<<"Datos del alumno:"<<endl;
            cout<<"1.Carnet :"<<aux->carnet<<endl;
            cout<<"2.DPI :"<<aux->dpi<<endl;
            cout<<"3.Nombre :"<<aux->nombre<<endl;
            cout<<"4.Carrera :"<<aux->carrera<<endl;
            cout<<"5.Correo :"<<aux->correo<<endl;
            cout<<"6.Contraseña :"<<aux->pass<<endl;
            cout<<"7.Creditos :"<<aux->creditos<<endl;
            cout<<"8.Edad :"<<aux->edad<<endl;
            cout<<"Seleccione dato a modificar: "<<endl;
            int modi =0;
            cin>>modi;
            switch(modi){
                case 1:{
                cout<<"Ingrese nuevo carnet: ";
                int pivo = 0;
                cin>>pivo;
                cout<<endl;
                aux->carnet= pivo;
                break;}
                case 2:{
                cout<<"Ingrese nuevo DPI: ";
                int  pivo2 = 0;
                cin>>pivo2;
                cout<<endl;
                aux->dpi= pivo2;
                break;}
                case 3:{
                cout<<"Ingrese nuevo nombre: ";
                string pivo = "";
                cin>>pivo;
                cout<<endl;
                aux->nombre= pivo;
                break;}
                case 4:{
                cout<<"Ingrese nueva carrera: ";
                string pivo = "";
                cin>>pivo;
                cout<<endl;
                aux->carrera= pivo;
                break;}
                case 5:{
                cout<<"Ingrese nuevo correo: ";
                string pivo = "";
                cin>>pivo;
                cout<<endl;
                aux->correo= pivo;
                break;}
                case 6:{
                cout<<"Ingrese nuevo contraseña: ";
                string pivo = "";
                cin>>pivo;
                cout<<endl;
                aux->pass= pivo;
                break;}
                case 7:{
                cout<<"Ingrese creditos: ";
                int pivo = 0;
                cin>>pivo;
                cout<<endl;
                aux->creditos= pivo;
                break;}
                case 8:{
                cout<<"Ingrese edad: ";
                int pivo = 0;
                cin>>pivo;
                cout<<endl;
                aux->edad= pivo;
                break;}

            }//end switch
            cout<<"Cambio realizado con exito"<<endl;
           return 0;


        }//end if

        aux=aux->siguiente;
        au++;

    }
        cout<<"DPI no existe"<<endl;

         return 0;
}// end modificar
int ListaA::EliminarA(int dpi_){
    //me quedo aqui para el metodo de eliminar, hay que cambiar el dpi a long en vez de int. seguimos con las demas edd's y posterior a ver que tal nos va,animo

}

ListaA::~ListaA()
{
    //dtor
}
