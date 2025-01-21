
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CategorizedPhysicalQuantityModule import CategorizedPhysicalQuantity







class Extensive(CategorizedPhysicalQuantity):
    """
    Class representing the `Extensive` entity, which inherits from:
    - CategorizedPhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_194100e1_e11a_4b7c_bb5a_171655679fc8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Extensive'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Extensive(
    
    class_iri='https://w3id.org/emmo#EMMO_194100e1_e11a_4b7c_bb5a_171655679fc8',
    
    class_name='Extensive',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_194100e1_e11a_4b7c_bb5a_171655679fc8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Extensive',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    