
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LiquidElectrolyteModule import LiquidElectrolyte







class NonAqueousElectrolyte(LiquidElectrolyte):
    """
    Class representing the `NonAqueousElectrolyte` entity, which inherits from:
    - LiquidElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5f9a9411_05f9_4576_acd3_81d7d41cfe98'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NonAqueousElectrolyte'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NonAqueousElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5f9a9411_05f9_4576_acd3_81d7d41cfe98',
    
    class_name='NonAqueousElectrolyte',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5f9a9411_05f9_4576_acd3_81d7d41cfe98',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NonAqueousElectrolyte',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    