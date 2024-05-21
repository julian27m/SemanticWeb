export class Articulo {
    id: number;
    nombre: string;
    ruta_pdf: string;
    autor_id?: number;
    nombre_autor?: string;
  
    public constructor(id: number, nombre: string, ruta_pdf: string, autor_id: number, nombre_autor: string) {
      this.id = id;
      this.nombre = nombre;
      this.ruta_pdf = ruta_pdf;
      this.autor_id = autor_id;
      this.nombre_autor = nombre_autor;
    }
  
  }
  