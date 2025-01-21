
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturedMaterialModule import ManufacturedMaterial







class CarbonFelt(ManufacturedMaterial):
    """
    Class representing the `CarbonFelt` entity, which inherits from:
    - ManufacturedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1c530688_ee63_4683_b38f_80cce7ca75c1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CarbonFelt'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CarbonFelt(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1c530688_ee63_4683_b38f_80cce7ca75c1',
    
    class_name='CarbonFelt',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1c530688_ee63_4683_b38f_80cce7ca75c1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CarbonFelt',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    