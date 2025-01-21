
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EMMOModule import EMMO







class Item(EMMO):
    """
    Class representing the `Item` entity, which inherits from:
    - EMMO

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_eb3a768e_d53e_4be9_a23b_0714833c36de'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Item'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Item(
    
    class_iri='https://w3id.org/emmo#EMMO_eb3a768e_d53e_4be9_a23b_0714833c36de',
    
    class_name='Item',
    
    definition="example_value",
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_eb3a768e_d53e_4be9_a23b_0714833c36de',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Item',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    