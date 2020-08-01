import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { InputComponent } from './input/input.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatSelectModule } from '@angular/material/select';
import { MatDividerModule } from '@angular/material/divider';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTabsModule } from '@angular/material/tabs';
import { MatIconModule } from '@angular/material/icon';
import { MatTooltipModule } from '@angular/material/tooltip';
import { CodeComponent } from './code/code.component';
import { MonacoEditorModule, NgxMonacoEditorConfig } from 'ngx-monaco-editor';
import { FormsModule } from '@angular/forms';
import { ImportComponent } from './import/import.component';
import { ExportComponent } from './export/export.component';
import { CircuitComponent } from './circuit/circuit.component';
import { ConvertComponent } from './convert/convert.component';
import { GraphicalComponent } from './graphical/graphical.component';
import { HttpClientModule } from '@angular/common/http';


const monacoConfig: NgxMonacoEditorConfig = {
  baseUrl: 'assets',
  defaultOptions: { scrollBeyondLastLine: false }
};


@NgModule({
  declarations: [
    AppComponent,
    InputComponent,
    CodeComponent,
    ImportComponent,
    ExportComponent,
    CircuitComponent,
    ConvertComponent,
    GraphicalComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    MatButtonModule,
    MatInputModule,
    MatAutocompleteModule,
    MatSelectModule,
    MatDividerModule,
    MatToolbarModule,
    MatTabsModule,
    MatIconModule,
    MatTooltipModule,
    FormsModule,
    MonacoEditorModule.forRoot(),
    HttpClientModule


  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }