
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumSaltCompoundModule import CalciumSaltCompound







class CalciumTrifluoromethanesulfonyloxalatoborate(CalciumSaltCompound):
    """
    Class representing the `CalciumTrifluoromethanesulfonyloxalatoborate` entity, which inherits from:
    - CalciumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_dd8823eb_ea6f_49f2_a4f9_d21828cb8b8e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumTrifluoromethanesulfonyloxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumTrifluoromethanesulfonyloxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_dd8823eb_ea6f_49f2_a4f9_d21828cb8b8e',
    
    class_name='CalciumTrifluoromethanesulfonyloxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_dd8823eb_ea6f_49f2_a4f9_d21828cb8b8e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumTrifluoromethanesulfonyloxalatoborate',
        alias="class_name"
    )
    

    
    

    

    