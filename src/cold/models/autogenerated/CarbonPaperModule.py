
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturedMaterialModule import ManufacturedMaterial







class CarbonPaper(ManufacturedMaterial):
    """
    Class representing the `CarbonPaper` entity, which inherits from:
    - ManufacturedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd615729_8240_487a_a619_cc94656731f2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CarbonPaper'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CarbonPaper(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd615729_8240_487a_a619_cc94656731f2',
    
    class_name='CarbonPaper',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd615729_8240_487a_a619_cc94656731f2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CarbonPaper',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    