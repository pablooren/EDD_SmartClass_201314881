#ifndef LISTAA_H
#define LISTAA_H
#include "Alumno.h"

class ListaA
{
    public:
        ListaA();
        void IngresarA(int carnet_,int dpi_,string nombre_,string carrera_,string correo_,string pass_,int creditos_,int edad);
        int ModificarA(int dpi_);
        int EliminarA(int dpi_);
        bool ExisteA(int carnet_);
        void GraficarL();
        bool ListaVacia();
        void MostrarL();


        virtual ~ListaA();

    protected:

    private:
        alumno* inicio;
        alumno* fin;
        int tam;

};

#endif // LISTAA_H
