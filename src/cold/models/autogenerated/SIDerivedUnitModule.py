
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DerivedUnitModule import DerivedUnit



from .SIUnitModule import SIUnit







class SIDerivedUnit(DerivedUnit, SIUnit):
    """
    Class representing the `SIDerivedUnit` entity, which inherits from:
    - DerivedUnit, SIUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_59e710f4_d9ea_4167_9a3f_f90628a307df'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIDerivedUnit'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIDerivedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_59e710f4_d9ea_4167_9a3f_f90628a307df',
    
    class_name='SIDerivedUnit',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_59e710f4_d9ea_4167_9a3f_f90628a307df',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIDerivedUnit',
        alias="class_name"
    )
    

    
    

    

    