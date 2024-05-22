export class Articulo {
    id: number;
    nombre: string;
    ruta_pdf: string;
    autor_id?: number;
    nombre_autor?: string;
    referencias?: string;  // Nuevo atributo para referencias

    public constructor(id: number, nombre: string, ruta_pdf: string, autor_id: number, nombre_autor: string, referencias?: string) {
        this.id = id;
        this.nombre = nombre;
        this.ruta_pdf = ruta_pdf;
        this.autor_id = autor_id;
        this.nombre_autor = nombre_autor;
        this.referencias = referencias;
    }
}
