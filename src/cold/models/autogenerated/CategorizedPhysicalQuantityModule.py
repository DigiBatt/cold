
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalQuantityModule import PhysicalQuantity







class CategorizedPhysicalQuantity(PhysicalQuantity):
    """
    Class representing the `CategorizedPhysicalQuantity` entity, which inherits from:
    - PhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_79751276_b2d0_4e2f_bbd4_99d412f43d55'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CategorizedPhysicalQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CategorizedPhysicalQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_79751276_b2d0_4e2f_bbd4_99d412f43d55',
    
    class_name='CategorizedPhysicalQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_79751276_b2d0_4e2f_bbd4_99d412f43d55',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CategorizedPhysicalQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    