import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from './core/guards/auth.guard';

import { AuthComponent } from './layout/auth/auth.component';
import { AdminComponent } from './layout/admin/admin.component';

const routes: Routes = [
  { path: '', redirectTo: 'auth/login', pathMatch: 'full' },
  {
    path: 'dashboard', component: AdminComponent, canActivate: [AuthGuard],
    children: [
      { path: '', loadChildren: './layout/admin/admin.module#AdminModule' }
    ]
  },
  { path: '', component: AuthComponent,
    children: [
      { path: '', loadChildren: './layout/auth/auth.module#AuthModule' }
    ]
  },

  { path: 'error', component: AuthComponent,
    children: [
      { path: '', loadChildren: './layout/error/error.module#ErrorModule' }
    ]
  },

  { path: '**', redirectTo: 'dashboard' }
];

export const AppRoutingModule = RouterModule.forRoot(routes);
