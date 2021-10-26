#ifndef ALUMNO_H
#define ALUMNO_H
#include<iostream>
#include<stdlib.h>

using namespace std;


class alumno
{
    public:
        //constructores
        alumno();
        alumno(int carnet_,int dpi_,string nombre_,string carrera_,string correo_,string pass_,int creditos_,int edad, alumno *anterior,alumno *siguiente);
        int carnet,dpi,creditos,edad;
        string nombre,carrera,correo,pass;
        alumno *anterior,*siguiente;


        virtual ~alumno();

    protected:

    private:
};

#endif // ALUMNO_H
