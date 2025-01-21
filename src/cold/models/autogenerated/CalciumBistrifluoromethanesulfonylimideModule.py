
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumSaltCompoundModule import CalciumSaltCompound







class CalciumBistrifluoromethanesulfonylimide(CalciumSaltCompound):
    """
    Class representing the `CalciumBistrifluoromethanesulfonylimide` entity, which inherits from:
    - CalciumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_d30fb481_a68d_496f_9be3_0e78aef3ef32'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumBistrifluoromethanesulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumBistrifluoromethanesulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_d30fb481_a68d_496f_9be3_0e78aef3ef32',
    
    class_name='CalciumBistrifluoromethanesulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_d30fb481_a68d_496f_9be3_0e78aef3ef32',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumBistrifluoromethanesulfonylimide',
        alias="class_name"
    )
    

    
    

    

    