import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
    name: 'inputFilter',
    pure: false
})
export class InputFilterPipe implements PipeTransform {

    transform(items: any[], filter: String): any {
        if (!items || !filter) {
            return items;
        }
        // filter items array, items which match and return true will be
        // kept, false will be filtered out
        return items.filter(function(c){ return c._user.username == filter });
    }
}