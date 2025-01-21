
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturedMaterialModule import ManufacturedMaterial







class PerforatedFoil(ManufacturedMaterial):
    """
    Class representing the `PerforatedFoil` entity, which inherits from:
    - ManufacturedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c84a1d8f_e405_42ba_8c80_bbe3b9c6c66a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PerforatedFoil'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PerforatedFoil(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c84a1d8f_e405_42ba_8c80_bbe3b9c6c66a',
    
    class_name='PerforatedFoil',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c84a1d8f_e405_42ba_8c80_bbe3b9c6c66a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PerforatedFoil',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    