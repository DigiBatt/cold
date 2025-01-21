
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class CurrentChangeLimit(ElectrochemicalControlQuantity):
    """
    Class representing the `CurrentChangeLimit` entity, which inherits from:
    - ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_71f10616_15eb_4dc4_bc8d_ffaac3838af2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentChangeLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CurrentChangeLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_71f10616_15eb_4dc4_bc8d_ffaac3838af2',
    
    class_name='CurrentChangeLimit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_71f10616_15eb_4dc4_bc8d_ffaac3838af2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentChangeLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    