
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode







class IndicatorElectrode(ActiveElectrode, Electrode):
    """
    Class representing the `IndicatorElectrode` entity, which inherits from:
    - ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6fcd255_248d_4603_b128_04dab960a676'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IndicatorElectrode'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IndicatorElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6fcd255_248d_4603_b128_04dab960a676',
    
    class_name='IndicatorElectrode',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6fcd255_248d_4603_b128_04dab960a676',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IndicatorElectrode',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    