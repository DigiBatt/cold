
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InertElectrodeModule import InertElectrode







class HydrogenElectrode(InertElectrode):
    """
    Class representing the `HydrogenElectrode` entity, which inherits from:
    - InertElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c4a778c7_33da_4e1a_960e_402a210bfeff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HydrogenElectrode'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HydrogenElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c4a778c7_33da_4e1a_960e_402a210bfeff',
    
    class_name='HydrogenElectrode',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c4a778c7_33da_4e1a_960e_402a210bfeff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HydrogenElectrode',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    