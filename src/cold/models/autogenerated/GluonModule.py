
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GaugeBosonModule import GaugeBoson







class Gluon(GaugeBoson):
    """
    Class representing the `Gluon` entity, which inherits from:
    - GaugeBoson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7db59e56_f68b_48b7_ae99_891c35ae5c3b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Gluon'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Gluon(
    
    class_iri='https://w3id.org/emmo#EMMO_7db59e56_f68b_48b7_ae99_891c35ae5c3b',
    
    class_name='Gluon',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7db59e56_f68b_48b7_ae99_891c35ae5c3b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Gluon',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    