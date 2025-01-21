
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CategorizedPhysicalQuantityModule import CategorizedPhysicalQuantity







class ElectrochemicalQuantity(CategorizedPhysicalQuantity):
    """
    Class representing the `ElectrochemicalQuantity` entity, which inherits from:
    - CategorizedPhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aecc6094_c6a5_4a36_a825_8a497a2ae112'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalQuantity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aecc6094_c6a5_4a36_a825_8a497a2ae112',
    
    class_name='ElectrochemicalQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aecc6094_c6a5_4a36_a825_8a497a2ae112',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    