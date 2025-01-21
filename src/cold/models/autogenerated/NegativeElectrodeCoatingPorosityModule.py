
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PorosityModule import Porosity







class NegativeElectrodeCoatingPorosity(Porosity):
    """
    Class representing the `NegativeElectrodeCoatingPorosity` entity, which inherits from:
    - Porosity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5cb403c4_4f28_46cb_81c4_21c5c47ef14a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeElectrodeCoatingPorosity'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NegativeElectrodeCoatingPorosity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5cb403c4_4f28_46cb_81c4_21c5c47ef14a',
    
    class_name='NegativeElectrodeCoatingPorosity',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5cb403c4_4f28_46cb_81c4_21c5c47ef14a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeElectrodeCoatingPorosity',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    