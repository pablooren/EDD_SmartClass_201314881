#include "alumno.h"

alumno::alumno()
{
    this->carnet =0;
    this->carrera ="";
    this->correo="";
    this->creditos=0;
    this->dpi=0;
    this->edad=0;
    this->nombre="";
    this->pass="";
    this->anterior = nullptr;
    this->siguiente = nullptr;

    //ctor
}

alumno::insertarA(int carnet_,int dpi_,string nombre_,string carrera_,string correo_,string pass_,int creditos_,int edad, alumno *anterior,alumno *siguiente){

    this->carnet=carnet_;
    this->dpi = dpi_;
    this->nombre = nombre_;
    this->carrera = carrera_;
    this->correo=correo_;
    this->pass = pass_;
    this->creditos = creditos_;

}

alumno::~alumno()
{
    //dtor
}
