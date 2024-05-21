import { Component } from '@angular/core';
import { ArticuloService } from '../articulo.service';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-articulo-crear',
  templateUrl: './articulo-crear.component.html',
  styleUrls: ['./articulo-crear.component.css']
})
export class ArticuloCrearComponent {
  articuloForm: FormGroup;

  constructor(private articuloService: ArticuloService, private fb: FormBuilder) {
    this.articuloForm = this.fb.group({
      archivo: [null]
    });
  }

  onFileSelected(event: any) {
    const file = event.target.files[0];
    this.articuloForm.patchValue({
      archivo: file
    });
  }

  onSubmit() {
    if (this.articuloForm.get('archivo')?.value) {
      this.articuloService.crearArticulo(this.articuloForm.get('archivo')?.value).subscribe(
        response => {
          console.log('Artículo creado exitosamente', response);
        },
        error => {
          console.error('Error al crear el artículo', error);
        }
      );
    }
  }
}
